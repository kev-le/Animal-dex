# This script should be run while docker is running
# Instructions

# docker-compose up
# docker ps
# docker exec -t -i <app_id> bash
# cd cmpt470
# python manage.py shell
# paste code below

from animals.models import Animal

import csv

with open('../data/code/cats.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        # print(row['name'])
        # print(row['image'])
        _, created = Animal.objects.get_or_create(
            animal_breed=row['name'],
            image_url=row['image']
        )