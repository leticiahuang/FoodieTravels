from django.db import models
# from smart_selects.db_fields import ChainedForeignKey
from cities_light.models import Country, City

# Create your models here.

class Destinations(models.Model):
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True) 
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)

    #what you return is the name you see on admin site
    def __str__(self):
        return f"{self.country}, {self.city}"

class Users(models.Model):
    username = models.CharField(max_length=100)
    destinations = models.ManyToManyField(Destinations)

    def __str__(self):
        return f"{self.username}"


