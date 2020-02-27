from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search_by_term, name='search', kwargs={"search_type":'animal'}),
    path('<str:search_type>/search', views.search_by_term, name='specsearch'),
    re_path(r'^(?P<search_type>[a-zA-Z]*)/?search/(?P<letter>[a-zA-Z])$', views.index_search, name='index_search'),
    path('cat/', views.cats, name='cats'),
    path('dog/', views.dogs, name='dogs'),
    path('bird/', views.birds, name='birds'),
    path('cat/<slug:slug>', views.cat_detail, name='cat_detail'),
    path('dog/<slug:slug>', views.dog_detail, name='dog_detail'),
    path('bird/<slug:slug>', views.bird_detail, name='bird_detail'),
    path('<str:animal_type>/<slug:slug>/spot', views.spot, name='spot'),
    path('<str:animal_type>/<slug:slug>/unspot', views.unspot, name='unspot'),
    path('spotted', views.all_spotted, name='all_spotted'),
]
