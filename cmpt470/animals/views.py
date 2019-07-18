from django.shortcuts import render
from django.http import HttpResponse

from .models import Animal

# Create your views here.

def index(request):
    all_animals = Animal.objects.order_by('-name')
    context = {'all_animals': all_animals}
    return render(request, 'animals/index.html', context)