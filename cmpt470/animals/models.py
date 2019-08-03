from django.template.defaultfilters import slugify

from django.db import models

# to make a new model and migrations:
# docker exec -it containerID bash
# python3 ./cmpt470/manage.py makemigrations
# python3 ./cmpt470/manage.py migrate
# then docker-compose build && docker-compose up

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image_url = models.CharField(max_length=800) # image urls are rly long
    summary = models.CharField(max_length=4000)

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(Animal, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Cat(Animal):
    other_names = models.CharField(max_length=400, default=None, blank=True, null=True)
    nicknames = models.CharField(max_length=400, default=None, blank=True, null=True)
    origin = models.CharField(max_length=200, default=None, blank=True, null=True)

    def display(self):
        return {"Other Names:": self.other_names, "Nicknames:": self.nicknames, "Origin:": self.origin}

class Dog(Animal):
    other_names = models.CharField(max_length=1500, default=None, blank=True, null=True)
    nicknames = models.CharField(max_length=1500, default=None, blank=True, null=True)
    origin = models.CharField(max_length=500, default=None, blank=True, null=True)
    weight = models.CharField(max_length=500, default=None, blank=True, null=True)
    height = models.CharField(max_length=500, default=None, blank=True, null=True)
    coat = models.CharField(max_length=500, default=None, blank=True, null=True)
    color = models.CharField(max_length=500, default=None, blank=True, null=True)
    lifespan = models.CharField(max_length=500, default=None, blank=True, null=True)

    def display(self):
        return {"Other Names:": self.other_names, "Nicknames:": self.nicknames, "Origin:": self.origin,
                "Weight:": self. weight, "Height": self.height, "Coat:": self. coat, "Color:": self. color,
                "Lifespan:": self.lifespan}

class Bird(Animal):
    conservation_status = models.CharField(max_length=200, default=None, blank=True, null=True)
    kingdom = models.CharField(max_length=200, default=None, blank=True, null=True)
    phylum = models.CharField(max_length=200, default=None, blank=True, null=True)
    scientific_class = models.CharField(max_length=200, default=None, blank=True, null=True)
    order = models.CharField(max_length=200, default=None, blank=True, null=True)
    family = models.CharField(max_length=200, default=None, blank=True, null=True)
    binomial_name = models.CharField(max_length=200, default=None, blank=True, null=True)

    def display(self):
        return {"Conservation Status:": self.conservation_status, "Kingdom:": self.kingdom, "Phylum:": self.phylum,
                "Scientific Class:": self. scientific_class, "Order": self.order, "Family:": self.family, "Binomial Name": self.binomial_name}
