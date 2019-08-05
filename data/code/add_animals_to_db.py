# This script should be run while docker is running
# Instructions

# docker-compose up
# docker ps
# docker exec -t -i <app_id> bash
# cd cmpt470
# python manage.py shell
# paste code below

import csv

from animals.models import Cat, Dog, Bird

def get_row(row):
    row = row.strip()
    if len(row) > 0:
        return row
    return None

# Cats
with open('../data/code/cat.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        breed = get_row(row['breed'])
        summary = get_row(row['summary'])
        image = get_row(row['image'])
        other_names = get_row(row['other_names'])
        nicknames = get_row(row['nicknames'])
        origin = get_row(row['origin'])
        _, created = Cat.objects.get_or_create(
            name=breed,
            image_url=image,
            summary=summary,
            other_names=other_names,
            nicknames=nicknames,
            origin=origin
        )
    
# Dogs
# (Paste after above)
with open('../data/code/dog.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        breed = get_row(row['breed'])
        summary = get_row(row['summary'])
        image = get_row(row['image'])
        other_names = get_row(row['other_names'])
        nicknames = get_row(row['nicknames'])
        origin = get_row(row['origin'])
        weight = get_row(row['weight'])
        height = get_row(row['height'])
        coat = get_row(row['coat'])
        color = get_row(row['color'])
        lifespan = get_row(row['lifespan'])
        _, created = Dog.objects.get_or_create(
            name=breed,
            image_url=image,
            summary=summary,
            other_names=other_names,
            nicknames=nicknames,
            origin=origin,
            weight=weight,
            height=height,
            coat=coat,
            color=color,
            lifespan=lifespan
        )

# Birds
# (Paste after above)
with open('../data/code/bird.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        breed = get_row(row['breed'])
        summary = get_row(row['summary'])
        image = get_row(row['image'])
        conservation_status = get_row(row['conservation_status'])
        kingdom = get_row(row['kingdom'])
        phylum = get_row(row['phylum'])
        order = get_row(row['order'])
        family = get_row(row['family'])
        binomial_name = get_row(row['binomial_name'])
        _, created = Bird.objects.get_or_create(
            name=breed,
            image_url=image,
            summary=summary,
            conservation_status=conservation_status,
            kingdom=kingdom,
            phylum=phylum,
            order=order,
            family=family,
            binomial_name=binomial_name
        )