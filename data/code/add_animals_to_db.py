# This script should be run while docker is running
# Instructions

# docker-compose up
# docker ps
# docker exec -t -i <app_id> bash
# cd cmpt470
# python manage.py shell
# paste code below

import csv

from animals.models import Cat, Dog

with open('../data/code/cats.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        _, created = Cat.objects.get_or_create(
            name=row['name'],
            image_url=row['image'],
            summary='This is an animal'
        )

# This is the same as Cats for now, but will be different later
with open('../data/code/dogs.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        _, created = Dog.objects.get_or_create(
            name=row['name'],
            image_url=row['image'],
            summary='This is an animal'
        )