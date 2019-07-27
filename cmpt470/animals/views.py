from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Animal, Dog, Cat, Bird

# Create your views here.

def index(request):
    animal_list = Animal.objects.order_by('name')

    page = request.GET.get('page', 1)
    paginator = Paginator(animal_list, 20)
    try:
        animals = paginator.page(page)
    except PageNotAnInteger:
        animals = paginator.page(1)
    except EmptyPage:
        animals = paginator.page(paginator.num_pages)

    context = {'animals': animals, 'page_title': 'All Animals', 'search_action': '/animals/search', 'placeholder': 'Search for animals'}
    return render(request, 'animals/index.html', context)

def detail(request, animal):
    context = {'animal': animal, 'animal_dict': animal.display()}
    return render(request, 'animals/detail.html', context)

def cats(request):
    animal_list = Cat.objects.order_by('name')

    page = request.GET.get('page', 1)
    paginator = Paginator(animal_list, 20)
    try:
        animals = paginator.page(page)
    except PageNotAnInteger:
        animals = paginator.page(1)
    except EmptyPage:
        animals = paginator.page(paginator.num_pages)

    context = {'animals': animals, 'page_title': 'Cats', 'search_action': '/animals/cat/search', 'placeholder': 'Search for cats'}
    return render(request, 'animals/index.html', context)

def dogs(request):
    animal_list = Dog.objects.order_by('name')

    page = request.GET.get('page', 1)
    paginator = Paginator(animal_list, 20)
    try:
        animals = paginator.page(page)
    except PageNotAnInteger:
        animals = paginator.page(1)
    except EmptyPage:
        animals = paginator.page(paginator.num_pages)

    context = {'animals': animals, 'page_title': 'Dogs', 'search_action': '/animals/dog/search', 'placeholder': 'Search for dogs'}
    return render(request, 'animals/index.html', context)

def birds(request):
    animal_list = Bird.objects.order_by('name')

    page = request.GET.get('page', 1)
    paginator = Paginator(animal_list, 20)
    try:
        animals = paginator.page(page)
    except PageNotAnInteger:
        animals = paginator.page(1)
    except EmptyPage:
        animals = paginator.page(paginator.num_pages)
    
    context = {'animals': animals, 'page_title': 'Birds', 'search_action': '/animals/bird/search', 'placeholder': 'Search for birds'}
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
        page_title = "Search for All Animals: '" + search_term + "'"

        animal_list = Animal.objects.filter(name__icontains=search_term).order_by('name')  #icontains=case-insensitive

        page = request.GET.get('page', 1)
        paginator = Paginator(animal_list, 20)
        try:
            animals = paginator.page(page)
        except PageNotAnInteger:
            animals = paginator.page(1)
        except EmptyPage:
            animals = paginator.page(paginator.num_pages)
        
        context = {'animals': animals, 'search_term': search_term, 'page_title': page_title}
        return render(request, 'animals/index.html', context)

def specific_search(request, search_type):
    search_term = request.GET['q']

    if search_term == '':   #if no search term, redirect to animal index page
        return HttpResponseRedirect('/animals/')
    else:   #if search term exists, show search results
        page_title = "Search for " + search_type + " '" + search_term + "'"

        if search_type == 'cat':
            animal_list = Cat.objects.filter(name__icontains=search_term).order_by('name')
        elif search_type == 'dog':
            animal_list = Dog.objects.filter(name__icontains=search_term).order_by('name') 
        elif search_type == 'bird':
            animal_list = Bird.objects.filter(name__icontains=search_term).order_by('name')
        else:
            animal_list = Animal.objects.filter(name__icontains=search_term).order_by('name') 

        page = request.GET.get('page', 1)
        paginator = Paginator(animal_list, 20)
        try:
            animals = paginator.page(page)
        except PageNotAnInteger:
            animals = paginator.page(1)
        except EmptyPage:
            animals = paginator.page(paginator.num_pages)
        
        context = {'animals': animals, 'search_term': search_term, 'page_title': page_title}
        return render(request, 'animals/index.html', context)
