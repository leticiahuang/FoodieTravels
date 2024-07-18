from django.contrib import admin
from .models import Users, Countries, Destinations

# Register your models here.
admin.site.register(Users)
admin.site.register(Countries)
admin.site.register(Destinations)