# Generated by Django 5.0.6 on 2024-08-04 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getFoods', '0022_alter_food_resto_latitude_alter_food_resto_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='resto_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]