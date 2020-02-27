from django.contrib import admin
from .models import Pet, Rating

# Register your models here.
admin.site.register(Pet)
admin.site.register(Rating)