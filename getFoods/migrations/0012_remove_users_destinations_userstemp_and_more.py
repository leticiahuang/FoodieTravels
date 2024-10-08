# Generated by Django 5.0.6 on 2024-07-24 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cities_light', '0011_alter_city_country_alter_city_region_and_more'),
        ('getFoods', '0011_remove_users_destinations_delete_destinations_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='destinations',
        ),
        migrations.CreateModel(
            name='UsersTemp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('city', models.ManyToManyField(blank=True, null=True, to='cities_light.city')),
            ],
        ),
        migrations.AddField(
            model_name='users',
            name='destinations',
            field=models.ManyToManyField(to='cities_light.city'),
        ),
    ]
