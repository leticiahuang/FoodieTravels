from django.db import models

# Create your models here.

class Countries(models.Model):
    countryName = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.countryName}"
    
class Users(models.Model):
    name = models.CharField(max_length=100)
    countriesSelected = models.ManyToManyField(Countries)

    def __str__(self):
        return f"{self.name}"


