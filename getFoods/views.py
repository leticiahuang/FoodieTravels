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
    '''if request.user.is_authenticated:
        return render(request, "getFoods/planTrip.html")
    else:'''
    return HttpResponseRedirect(reverse('getFoods:login'))


def login_view(request):
    #if login info was filled
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        #if user exists, login
        if user: 
            login(request, user)
            return render(request, "getFoods/planTrip.html", {'username':username})

        else:
            return render(request, "getFoods/login.html", {'message' : "Wrong username or password."})

    #go to login page if new to site
    return render(request, "getFoods/login.html")

def logout_view(request):
    logout(request)
    return render(request, "getFoods/login.html", {'message': "Logged out."})

def planTrip(request, username):
    user = Users.objects.get(pk=username)
    
    #if new country submitted, add
    if request.method == "POST":
        user.countriesSelected.add(request.POST['newCountry'])
        

    return render(request, "getFoods/planTrip.html")
    '''
    form = NewRequest()
    return render(request, "getFoods/planTrip.html", {"form": form})



    username = request.POST['username']

        logger.info("received name=", username)

        user = Users(name=username)  
        user.save()

        # What you want to render
    '''