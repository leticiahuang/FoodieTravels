from django.urls import path

from . import views

app_name = "getFoods"
urlpatterns = [
    path("", views.index, name="index"),
    path("FoodPlan/", views.foodPlan, name="foodPlan"),
]