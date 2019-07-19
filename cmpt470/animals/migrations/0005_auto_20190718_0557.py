# Generated by Django 2.2.3 on 2019-07-18 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0004_auto_20190718_0136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bird',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='animals.Animal')),
                ('conservation_status', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('kingdom', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('phylum', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('scientific_class', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('order', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('family', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('genus', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('species', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('binomial_name', models.CharField(blank=True, default=None, max_length=200, null=True)),
            ],
            bases=('animals.animal',),
        ),
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='animals.Animal')),
                ('other_names', models.CharField(blank=True, default=None, max_length=400, null=True)),
                ('nicknames', models.CharField(blank=True, default=None, max_length=400, null=True)),
                ('origin', models.CharField(blank=True, default=None, max_length=200, null=True)),
            ],
            bases=('animals.animal',),
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('animal_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='animals.Animal')),
                ('other_names', models.CharField(blank=True, default=None, max_length=400, null=True)),
                ('nicknames', models.CharField(blank=True, default=None, max_length=400, null=True)),
                ('origin', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('weight', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('height', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('coat', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('color', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('lifespan', models.CharField(blank=True, default=None, max_length=200, null=True)),
            ],
            bases=('animals.animal',),
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='animal_breed',
            new_name='name',
        ),
        migrations.AddField(
            model_name='animal',
            name='summary',
            field=models.CharField(default='This is an animal', max_length=2000),
            preserve_default=False,
        ),
    ]