# Generated by Django 5.0.6 on 2024-08-04 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getFoods', '0020_rename_resto_location_x_food_resto_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='resto_latitude',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='resto_longitude',
            field=models.FloatField(null=True),
        ),
    ]
