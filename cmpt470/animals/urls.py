from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
    path('<str:search_type>/search', views.specific_search, name='specsearch'),
    path('cat/', views.cats, name='cats'),
    path('dog/', views.dogs, name='dogs'),
    path('bird/', views.birds, name='birds'),
    path('cat/<slug:slug>', views.cat_detail, name='cat_detail'),
    path('dog/<slug:slug>', views.dog_detail, name='dog_detail'),
    path('bird/<slug:slug>', views.bird_detail, name='bird_detail'),
    path('<str:animal_type>/<slug:slug>/spot', views.spot, name='spot'),
    path('spotted', views.all_spotted, name='all_spotted'),
]
