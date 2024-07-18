from django.db import models
# from smart_selects.db_fields import ChainedForeignKey
from cities_light.models import Country, City

# Create your models here.

class Countries(models.Model):
    country_name = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.country_name}"
    
class Users(models.Model):
    username = models.CharField(max_length=100)
    countries_selected = models.ManyToManyField(Countries, blank=True, related_name="visitors")
    #blank means users can have no countriesSelected, and can access users through Countries.visitors
    countries_not_selected = models.ManyToManyField(Countries, blank=True, related_name="non_visitors")

    def __str__(self):
        return f"{self.username}"

class Destinations(models.Model):
    pass
    def __str__(self):
        return f"{self.username}"
    # country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True) 
    # city = ChainedForeignKey(City, chained_field='country', chained_model_field='country')


#i think basically delete Countries and replace with Destinations


