from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Animal, Dog, Cat, Bird, Has_Spotted


def display_results(request, animal_list, context):
    animals_length = len(animal_list)

    page = request.GET.get('page', 1)
    paginator = Paginator(animal_list, 20)
    try:
        animals = paginator.page(page)
    except PageNotAnInteger:
        animals = paginator.page(1)
    except EmptyPage:
        animals = paginator.page(paginator.num_pages)

    context['animals'] = animals
    context['animals_length'] = animals_length

    return render(request, 'animals/index.html', context)


def index(request):
    animal_list = Animal.objects.order_by('name')

    context = {
        'page_title':'All Animals',
        'search_action': '/animals/search',
        'placeholder': 'Search for animals'
    }

    return display_results(request, animal_list, context)


def detail(request, animal):
    if request.user.is_authenticated:
        if Has_Spotted.objects.filter(user=request.user, animal=animal).exists():
            isSpotted = True
        else:
            isSpotted = False
    else:
        isSpotted = False

    context = {'animal': animal, 'animal_dict': animal.display(), 'isSpotted': isSpotted}
    return render(request, 'animals/detail.html', context)


def cats(request):
    animal_list = Cat.objects.order_by('name')

    context = {
        'page_title':'Cats',
        'search_action': '/animals/cat/search',
        'placeholder': 'Search for Cats'
    }
    return display_results(request, animal_list, context)



def dogs(request):
    animal_list = Dog.objects.order_by('name')

    context = {
        'page_title':'Dogs',
        'search_action': '/animals/dog/search',
        'placeholder': 'Search for Dogs'
    }
    return display_results(request, animal_list, context)


def birds(request):
    animal_list = Bird.objects.order_by('name')

    context = {
        'page_title':'Birds',
        'search_action': '/animals/bird/search',
        'placeholder': 'Search for Birds'
    }
    return display_results(request, animal_list, context)


def cat_detail(request, slug):
    animal = get_object_or_404(Cat, slug=slug)
    return detail(request, animal)

def dog_detail(request, slug):
    animal = get_object_or_404(Dog, slug=slug)
    return detail(request, animal)

def bird_detail(request, slug):
    animal = get_object_or_404(Bird, slug=slug)
    return detail(request, animal)



def search_by_term(request, search_type):
    search_term = request.GET['q']

    if search_term == '':   #if no search term, redirect to animal index page
        return HttpResponseRedirect('/animals/')
    else:   #if search term exists, show search results
        page_title = "Search for " + search_type + ": '" + search_term + "'"

        if search_type == 'cat':
            animal_list = Cat.objects.filter(name__icontains=search_term).order_by('name')
        elif search_type == 'dog':
            animal_list = Dog.objects.filter(name__icontains=search_term).order_by('name')
        elif search_type == 'bird':
            animal_list = Bird.objects.filter(name__icontains=search_term).order_by('name')
        else:
            animal_list = Animal.objects.filter(name__icontains=search_term).order_by('name')

        context = {
            'search_term': search_term,
            'page_title': page_title,
            'search_action': request.path
        }

        return display_results(request, animal_list, context)

@login_required(login_url='/users/login/')
def spot(request, animal_type, slug):
    animal = Animal.objects.get(slug=slug)

    #Check if record already exists in Has_Spotted table
    if not Has_Spotted.objects.filter(user=request.user, animal=animal).exists():
        new_has_spotted = Has_Spotted(user=request.user, animal=animal)
        new_has_spotted.save()

    #Select which page to redirect to
    if animal_type == 'cat':
        return HttpResponseRedirect(reverse('cat_detail', args=[slug]))
    elif animal_type == 'dog':
        return HttpResponseRedirect(reverse('dog_detail', args=[slug]))
    elif animal_type == 'bird':
        return HttpResponseRedirect(reverse('bird_detail', args=[slug]))
    else:
        raise Http404("Animal does not exist")

@login_required(login_url='/users/login/')
def all_spotted(request):
    spotted_animals = set()

    for spotted in Has_Spotted.objects.filter(user=request.user).select_related('animal'):
        # Without select_related(), this would make a database query for each
        # loop iteration in order to fetch the related animal for each entry.
        spotted_animals.add(spotted.animal)
    
    animals_count = len(spotted_animals)
    context = {'animals': spotted_animals, 'page_title': 'Your Spotted Animals', 'search_action': '/animals/search', 'placeholder': 'Search for animals', 'animals_length': animals_count}
    return render(request, 'animals/index.html', context)




def index_search(request, search_type='', letter=''):

    length = -len(letter)
    search_action = request.path[:-len(letter) - 1] # hacky way to get search action from url
    index_url = search_action[:-7]

    if search_type == 'cat':
        animal_list = Cat.objects.filter(name__istartswith=letter).order_by('name')
        page_title = "Cats starting with '" + letter + "'"
        placeholder = "Search for Cats"
    elif search_type == 'dog':
        animal_list = Dog.objects.filter(name__istartswith=letter).order_by('name')
        page_title = "Dogs starting with '" + letter + "'"
        placeholder = "Search for Dogs"
    elif search_type == 'bird':
        animal_list = Bird.objects.filter(name__istartswith=letter).order_by('name')
        page_title = "Birds starting with '" + letter + "'"
        placeholder = "Search for Birds"
    else:
        animal_list = Animal.objects.filter(name__istartswith=letter).order_by('name')
        page_title = "All animals starting with '" + letter + "'"
        placeholder = "Search for Animals"

    context = {
        'search_action': search_action,
        'page_title': page_title,
        'index_url' : index_url,
        'placeholder': placeholder,
    }

    return display_results(request, animal_list, context)
