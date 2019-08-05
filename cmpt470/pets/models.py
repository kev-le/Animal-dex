from django.db import models
from django.db.models import Avg
from django.conf import settings
from animals.models import Animal

# to make a new migration for a model:
# docker exec -it containerID bash
# python3 ./cmpt470/manage.py makemigrations
# python3 ./cmpt470/manage.py migrate
# then docker-compose build && docker-compose up

class Pet(models.Model):
    user       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    animal     = models.ForeignKey(Animal, on_delete='PROTECT')
    name       = models.CharField(max_length=100, default=None, blank=True, null=True)
    bio        = models.TextField(default=None, blank=True, null=True)
    user_image = models.ImageField(upload_to='images/')

    def get_average_rating(self):
        return self.rating_set.aggregate(Avg('scores')).get('scores__avg') # returns None if no ratings

    def get_number_of_ratings(self):
        return self.rating_set.count()

    def __str__(self):
        return self.name

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    pet = models.ForeignKey('Pet', on_delete=models.CASCADE)
    SCORE_CHOICES = (
        (1,1),(2,2),(3,3),(4,4),(5,5)
    )
    scores = models.IntegerField(choices=SCORE_CHOICES)
