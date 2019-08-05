from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

from .forms import create_pet_form

from .models import Pet, Rating
from animals.models import Animal, Cat, Dog, Bird

# Create your views here.

def pets_index(request):

    all_pets = sorted(Pet.objects.all(), key=lambda p: p.get_average_rating(), reverse=True)
    top_pets = all_pets[:5] # top 5 featured pets, based on rating
    recent_pets = all_pets[5:] # rest of pets
    
    context = {'top_pets': top_pets, 'recent_pets' : recent_pets}
    return render(request, 'pets/index.html', context)

# POST for rating
@login_required(login_url='/users/login')
def rating(request):
    if request.method == 'POST':
        print(request.POST)
        rating = request.POST.get('rating', None)
        petId = request.POST.get('petId', None)

        # get associated pet
        pet = Pet.objects.get(id=petId)
        if not pet:
            return HttpResponse("Pet not found!", status=500)
        else:
            print(request.POST)

            # create new Rating
            rating = Rating.objects.create(user=request.user, pet=pet, scores=rating)

            # create new rating for the pet
            pet.rating_set.add(rating)
            pet.save()

    return HttpResponse("Rating Submitted!")

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
    context = { 'pet' : pet }
    return render(request, 'pets/rate.html', context)
