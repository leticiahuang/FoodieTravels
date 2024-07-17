from django.urls import path

from . import views

app_name = "getFoods"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("plan_trip", views.plan_trip, name="plan_trip"),
    path("itinerary", views.itinerary, name="itinerary"),
    path("register", views.register, name="register"),
]