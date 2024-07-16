from django.urls import path

from . import views

app_name = "getFoods"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("planTrip", views.planTrip, name="planTrip"),
    path("itinerary", views.itinerary, name="itinerary"),
]