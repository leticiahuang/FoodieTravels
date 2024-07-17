from django.db import models

# Create your models here.

class Countries(models.Model):
    country_name = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.country_name}"
    
class Users(models.Model):
    username = models.CharField(max_length=100)
    countries_selected = models.ManyToManyField(Countries, blank=True, related_name="visitors")
    #blank means users can have no countriesSelected, and can access users through Countries.visitors

    def __str__(self):
        return f"{self.username}"


