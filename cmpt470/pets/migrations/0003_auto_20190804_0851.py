# Generated by Django 2.2.4 on 2019-08-04 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='animals',
            new_name='animal',
        ),
    ]
