from django.db import models
from django.conf import settings
from animals.models import Animal

# to make a new migration for a model:
# docker exec -it containerID bash
# python3 ./cmpt470/manage.py makemigrations
# python3 ./cmpt470/manage.py migrate
# then docker-compose build && docker-compose up

class Pet(models.Model):
    user       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    animals    = models.ForeignKey(Animal, on_delete='PROTECT')
    name       = models.CharField(max_length=100, default=None, blank=True, null=True)
    bio        = models.TextField(default=None, blank=True, null=True)
    user_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
