# Generated by Django 5.0.6 on 2024-08-04 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getFoods', '0019_remove_food_resto_location_food_resto_location_x_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='resto_location_x',
            new_name='resto_latitude',
        ),
        migrations.RenameField(
            model_name='food',
            old_name='resto_location_y',
            new_name='resto_longitude',
        ),
    ]