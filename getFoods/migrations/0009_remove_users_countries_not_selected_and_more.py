# Generated by Django 5.0.6 on 2024-07-23 03:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
        ('getFoods', '0008_rename_destination_destinations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='countries_not_selected',
        ),
        migrations.RemoveField(
            model_name='users',
            name='countries_selected',
        ),
        migrations.RemoveField(
            model_name='destinations',
            name='city',
        ),
        migrations.RemoveField(
            model_name='destinations',
            name='country',
        ),
        migrations.AddField(
            model_name='destinations',
            name='city_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities_light.city'),
        ),
        migrations.AddField(
            model_name='destinations',
            name='country_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities_light.country'),
        ),
        migrations.AddField(
            model_name='users',
            name='destinations',
            field=models.ManyToManyField(to='getFoods.destinations'),
        ),
        migrations.DeleteModel(
            name='Countries',
        ),
    ]