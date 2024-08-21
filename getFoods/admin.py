from django.contrib import admin
from .models import Users, Food, Restaurant

# Register your models here.
admin.site.register(Users)
admin.site.register(Food)
admin.site.register(Restaurant)