from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.pets_index, name='pets_index'),
    path('add_pet/', views.add_pet, name='add_pet'),
    path('rating/', views.rating, name='rating'),
    path('rate/<int:pet_id>', views.rate, name='rate'),
    path('edit/<int:pet_id>', views.edit_pet, name='edit')

]
