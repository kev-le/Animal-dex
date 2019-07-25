from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from .models import Animal, Dog, Cat, Bird

# Create your views here.

def index(request):
    animals = Animal.objects.order_by('name')[:75]
    context = {'animals': animals, 'page_title': 'All Animals', 'search_action': '/animals/search'}
    return render(request, 'animals/index.html', context)

def detail(request, animal):
    context = {'animal': animal, 'animal_dict': animal.display()}
    return render(request, 'animals/detail.html', context)

def cats(request):
    animals = Cat.objects.order_by('name')[:75]
    context = {'animals': animals, 'page_title': 'Cats', 'search_action': '/animals/cat/search'}
    return render(request, 'animals/index.html', context)

def dogs(request):
    animals = Dog.objects.order_by('name')[:75]
    context = {'animals': animals, 'page_title': 'Dogs', 'search_action': '/animals/dog/search'}
    return render(request, 'animals/index.html', context)

def birds(request):
    animals = Bird.objects.order_by('name')[:75]
    context = {'animals': animals, 'page_title': 'Birds', 'search_action': '/animals/bird/search'}
    return render(request, 'animals/index.html', context)

def cat_detail(request, slug):
    animal = get_object_or_404(Cat, slug=slug)

    return detail(request, animal)

def dog_detail(request, slug):
    animal = get_object_or_404(Dog, slug=slug)

    return detail(request, animal)

def bird_detail(request, slug):
    animal = get_object_or_404(Bird, slug=slug)

    return detail(request, animal)

def search(request):
    search_term = request.GET['q']

    if search_term == '':   #if no search term, redirect to animal index page
        return HttpResponseRedirect('/animals/')
    else:   #if search term exists, show search results
        page_title = "Search for '" + search_term + "'"

        animals = Animal.objects.filter(name__icontains=search_term).order_by('name')  #icontains=case-insensitive
        context = {'animals': animals, 'search_term': search_term, 'page_title': page_title}
        return render(request, 'animals/index.html', context)

def specific_search(request, search_type):
    search_term = request.GET['q']

    if search_term == '':   #if no search term, redirect to animal index page
        return HttpResponseRedirect('/animals/')
    else:   #if search term exists, show search results
        page_title = "Search for '" + search_term + "'"

        if search_type == 'cat':
            animals = Cat.objects.filter(name__icontains=search_term).order_by('name')
        elif search_type == 'dog':
            animals = Dog.objects.filter(name__icontains=search_term).order_by('name') 
        elif search_type == 'bird':
            animals = Bird.objects.filter(name__icontains=search_term).order_by('name')
        else:
            animals = Animal.objects.filter(name__icontains=search_term).order_by('name') 
        context = {'animals': animals, 'search_term': search_term, 'page_title': page_title}
        return render(request, 'animals/index.html', context)
