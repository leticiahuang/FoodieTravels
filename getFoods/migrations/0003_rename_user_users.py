# Generated by Django 5.0.6 on 2024-07-12 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('getFoods', '0002_rename_country_countries_countryname_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]