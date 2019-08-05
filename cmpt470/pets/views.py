from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage

from .models import Pet, Rating
from animals.models import Animal, Cat, Dog, Bird

# Create your views here.

def pets_index(request):

    pets = Pet.objects.all()
    
    context = {'pets': pets}
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


def add_pet(request):
    if request.method == 'POST':
        if (True): # TODO: check if post data is valid
            type = request.POST['animal_type']
            breed_id = request.POST['animal_breed']
            pet_name = request.POST['pet_name']
            pet_bio = request.POST['pet_bio']
            pet_image = request.FILES['pet_image']

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
            pet.save()
        return redirect('pets_index')
    
    dogs = Dog.objects.order_by('name')
    cats = Cat.objects.order_by('name')
    birds = Bird.objects.order_by('name')

    context = {
        'dogs': dogs,
        'cats': cats,
        'birds': birds
    }
    
    return render(request, 'pets/add_pet.html', context)

def rate(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    context = { 'pet' : pet }
    return render(request, 'pets/rate.html', context)