from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

from django.http import HttpResponseForbidden

from .forms import create_pet_form, edit_pet_form

from .models import Pet, Rating
from animals.models import Animal, Cat, Dog, Bird

from users.models import CustomUser

import json

def pets_index(request):

    all_pets = sorted(Pet.objects.all(), key=lambda p: (p.get_average_rating() * p.get_number_of_ratings()) , reverse=True)
    top_pets = all_pets[:5] # top 5 featured pets, based on rating
    recent_pets = Pet.objects.all().order_by('-pk')[:10]

    context = {'top_pets': top_pets, 'recent_pets' : recent_pets}
    return render(request, 'pets/index.html', context)

# POST for rating
@login_required(login_url='/users/login')
def rating(request):
    if request.method == 'POST':
        # print(request.POST)
        rating = request.POST.get('rating', None)
        petId = request.POST.get('petId', None)

        # get associated pet
        pet = Pet.objects.get(id=petId)
        if not pet:
            return HttpResponse("Pet not found!", status=500)
        else:
            # print(request.POST)

            # create new Rating
            rating = Rating.objects.create(user=request.user, pet=pet, scores=rating)

            # create new rating for the pet
            pet.rating_set.add(rating)
            pet.save()

    return HttpResponse("Rating Submitted!")

@login_required(login_url='/users/login')
def edit_pet(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if pet.user == request.user:

        if hasattr(pet.animal, "cat"):
            type = "Cat"
        elif hasattr(pet.animal, "dog"):
            type = "Dog"
        elif hasattr(pet.animal, "bird"):
            type = "Bird"

        if request.method == 'POST':
            form = edit_pet_form(request.POST, request.FILES)
            if form.is_valid():
                type = form.cleaned_data['animal_type']
                if type == 'Dog':
                    animal = Dog.objects.get(id=form.cleaned_data['animal_breed'])
                elif type == 'Cat':
                    animal = Cat.objects.get(id=form.cleaned_data['animal_breed'])
                elif type == 'Bird':
                    animal = Bird.objects.get(id=form.cleaned_data['animal_breed'])

                pet.name = form.cleaned_data['pet_name']
                pet.animal = animal
                pet.bio = form.cleaned_data['pet_bio']

                if form.cleaned_data['pet_image']:
                    pet.user_image = form.cleaned_data['pet_image']
                pet.save()

        dogs = Dog.objects.order_by('name')
        cats = Cat.objects.order_by('name')
        birds = Bird.objects.order_by('name')
        context = {
            'pet' : pet,
            'dogs': dogs,
            'cats': cats,
            'birds':birds,
            'type':type,
        }
        return render(request, 'pets/edit.html', context)
    else:
        return HttpResponseForbidden()



@login_required(login_url='/users/login')
def add_pet(request):
    if request.method == 'POST':

        form = create_pet_form(request.POST, request.FILES)

        if form.is_valid(): # TODO: check if post data is valid
            type = form.cleaned_data['animal_type']
            breed_id = form.cleaned_data['animal_breed']
            pet_name = form.cleaned_data['pet_name']
            pet_bio = form.cleaned_data['pet_bio']
            pet_image = form.cleaned_data['pet_image']

            if type == 'Dog':
                animal = Dog.objects.get(id=breed_id)
            elif type == 'Cat':
                animal = Cat.objects.get(id=breed_id)
            elif type == 'Bird':
                animal = Bird.objects.get(id=breed_id)

            pet = Pet.objects.create(
                user=request.user,
                animal=animal,
                name=pet_name,
                bio=pet_bio,
                user_image=pet_image
            )
            return redirect('pets_index')
    else:
        form = create_pet_form()

    dogs = Dog.objects.order_by('name')
    cats = Cat.objects.order_by('name')
    birds = Bird.objects.order_by('name')

    context = {
        'dogs': dogs,
        'cats': cats,
        'birds': birds,
        'form': form
    }

    return render(request, 'pets/add_pet.html', context)

@login_required(login_url='/users/login')
def rate(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)

    # check if user has rated this pet 
    if not Rating.objects.filter(user=request.user, pet=pet):
        user_already_rated = False
    else:
        user_already_rated = True

    context = { 'pet' : pet , 'user_already_rated' : user_already_rated }
    return render(request, 'pets/rate.html', context)


@login_required(login_url='/home')
def rate_view(request):

    if request.method == 'POST':
        rating = request.POST.get('rating', None)
        petId = request.POST.get('petId', None)

        # get associated pet to update its rating
        pet = Pet.objects.get(id=petId)
        if not pet:
            return HttpResponse("Pet not found!", status=500)
        else:
            # update last seen pet
            user = CustomUser.objects.get(id=request.user.id)
            user.rate_index = pet.id

            # make sure next pet actually exists
            next_pet = Pet.objects.filter(id__gt=pet.id).order_by('id').first()
            if not next_pet:
                next_pet = Pet.objects.filter(id__gte=1).order_by('id').first()
                user.rate_index = next_pet.id

            user.save()

            # create new Rating
            rating = Rating.objects.create(user=request.user, pet=pet, scores=rating)
            # create new rating for the pet
            pet.rating_set.add(rating)
            pet.save()


            context = {
                "id": next_pet.id,
                "name" : next_pet.name,
                "rating": next_pet.get_average_rating(),
                "bio": next_pet.bio,
                "url": next_pet.user_image.url,
             }
            return HttpResponse(json.dumps(context), content_type="application/json")

    # pet = get_object_or_404(Pet, id=request.user.rate_index)
    pet = Pet.objects.filter(id__gt=request.user.rate_index).order_by('id').first()

    if not pet:
        pet = Pet.objects.filter(id__gte=1).order_by('id').first()

    context = { 'pet' : pet }
    return render(request, 'pets/rate_view.html', context)
