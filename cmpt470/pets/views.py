from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Pet

# Create your views here.

def index(request):

    pets = Pet.objects.all()
    
    context = {'pets': pets}
    return render(request, 'pets/index.html', context)