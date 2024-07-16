from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Users, Countries
#from .forms import NewRequest
from django import forms
import logging
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
logger = logging.getLogger(__name__)

def index(request):
    return HttpResponseRedirect(reverse('getFoods:login'))


def login_view(request):
    #if login info was filled
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        #if user exists, login
        if user: 
            request.session['username'] = username
            login(request, user)
            return HttpResponseRedirect(reverse('getFoods:planTrip', kwargs={'username':username}))

        else:
            return render(request, "getFoods/login.html", {'message' : "Wrong username or password."})

    #go to login page if new to site
    return render(request, "getFoods/login.html")

def logout_view(request):
    logout(request)
    try:
        del request.session['username']
    except KeyError:
        pass
    return render(request, "getFoods/login.html", {'message' : "Logged out."})

def planTrip(request, username):
    user = Users.objects.get(name = username)
    countriesSelected = user.countriesSelected.all()
    countriesNotSelected = Countries.objects.raw("SELECT * FROM getFoods_countries WHERE NOT EXISTS (select countries_id from getFoods_users_countriesSelected WHERE getFoods_countries.id=getFoods_users_countriesSelected.countries_id)")
    
    #if new country submitted, add
    if request.method == "POST":
        country_id = int(request.POST['newCountry'])
        country = Countries.objects.get(pk = country_id)
        #add if country exists:
        user.countriesSelected.add(country)

    return render(request, "getFoods/planTrip.html", {
        'user' : user, 
        'countriesSelected' : countriesSelected,
        'countriesNotSelected' : countriesNotSelected
        })

def itinerary(request):
    return HttpResponse("Hello, world!")