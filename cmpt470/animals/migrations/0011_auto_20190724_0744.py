# Generated by Django 2.2.3 on 2019-07-24 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0010_auto_20190724_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='nicknames',
            field=models.CharField(blank=True, default=None, max_length=1500, null=True),
        ),
    ]
