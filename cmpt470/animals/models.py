from django.db import models

# Create your models here.
class Animal(models.Model):
    animal_breed = models.CharField(max_length=200)
    image_url = models.CharField(max_length=800) # image urls are rly long

    def __str__(self):
        return self.animal_breed