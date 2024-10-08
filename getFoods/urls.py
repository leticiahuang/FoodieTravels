from django.urls import path

from . import views, api

app_name = "getFoods"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("plan_trip", views.plan_trip, name="plan_trip"),
    path("itinerary", views.itinerary, name="itinerary"),
    path("register", views.register, name="register"),
    path("delete/<int:id>", views.delete, name='delete'),
    path("get_cities/<str:country>", api.get_cities, name='get_cities'),
    path("get_top_foods", api.get_top_foods, name='get_top_foods'),
    ]