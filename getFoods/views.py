from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Users, Destinations
import logging
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  
from .forms import RegisterForm  
from cities_light.models import Country, City
from django.http import JsonResponse
from django.core.serializers import serialize


# Create your views here.
logger = logging.getLogger(__name__)

def index(request):
    return HttpResponseRedirect(reverse('getFoods:login'))

def register(request):
    #POST: register user if page is submitted
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        #if valid, create user and redirect to login 
        if form.is_valid():
            #creates user for django admin
            form.save() 

            #create user for Users model
            username = request.POST['username']
            Users(username = username).save()
            user = Users.objects.get(username = username)
            messages.success(request, "Account created.")
            return HttpResponseRedirect(reverse('getFoods:login'))

        #if not valid, go to register page again with same form
        else:
            messages.error(request, "Please change inputs and try again.")
            return render(request, "getFoods/register.html", {'RegisterForm':form})
    
    #GET: else create new form and get user to register
    form = RegisterForm()
    return render(request, "getFoods/register.html", {'RegisterForm':form})


def login_view(request):
    #if login info was filled
    if request.method == 'POST':
        #VALIDATE DATA
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        #if user exists, login
        if user: 
            login(request, user)
            #set session cookie
            request.session['my_username'] = username
            return HttpResponseRedirect(reverse('getFoods:plan_trip'))

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

def plan_trip(request):
    user = Users.objects.get(username = request.session.get('my_username'))
    
    #if new country submitted, add
    if request.method == "POST":
        dest_country = Country.objects.get(name = request.POST['add-country'])
        dest_city = City.objects.get(name = request.POST['add-city'])

        new_dest = Destinations.objects.get(country = dest_country, city = dest_city)
        #don't need to check if new_dest already in user.destination, django doesn't allow
        user.destinations.add(new_dest)

    return render(request, "getFoods/plan_trip.html", {
        'user' : user,
        'countries' : Country.objects.all(),
        'cities' : City.objects.all(),
        })

def itinerary(request):
    return HttpResponse("Hello, world!")

def delete(request, id):
    #this view used to delete a destination from user.destinations
    user = Users.objects.get(username = request.session.get('my_username'))
    destination = Destinations.objects.get(id = id)
    user.destinations.remove(destination)
    return HttpResponseRedirect(reverse('getFoods:plan_trip'))

def get_cities(request, country):
    #this view used to filter cities depending on country chosen
    query_results = City.objects.filter(country__name = country)
    #fields specify which fields of the model to return
    #serialize creates json object, don't need to return JsonResponse or will be changed twice
    json_object = serialize("json", query_results, fields=['name']) 
    return HttpResponse(json_object, content_type="application/json")


