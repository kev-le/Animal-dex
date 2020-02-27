# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    rate_index = models.IntegerField(default=1)
    # add additional fields in here

    def __str__(self):
        return self.email
