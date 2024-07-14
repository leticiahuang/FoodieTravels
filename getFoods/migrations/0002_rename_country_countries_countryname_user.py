# Generated by Django 5.0.6 on 2024-07-11 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getFoods', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='countries',
            old_name='country',
            new_name='countryName',
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('countriesSelected', models.ManyToManyField(to='getFoods.countries')),
            ],
        ),
    ]