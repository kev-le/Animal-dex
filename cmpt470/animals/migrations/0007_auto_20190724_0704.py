# Generated by Django 2.2.3 on 2019-07-24 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0006_animal_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bird',
            name='genus',
        ),
        migrations.RemoveField(
            model_name='bird',
            name='species',
        ),
        migrations.AlterField(
            model_name='animal',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
