# Generated by Django 5.0.6 on 2024-08-03 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getFoods', '0017_food_resto_link_food_resto_name_food_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='resto_link',
        ),
        migrations.AddField(
            model_name='food',
            name='resto_location',
            field=models.CharField(max_length=500, null=True),
        ),
    ]