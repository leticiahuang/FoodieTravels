from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Users, Countries
import logging
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  
from .forms import RegisterForm  
from cities_light.models import Country, City



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
            user.countries_not_selected.add(*Countries.objects.all())
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
        add_country = Countries.objects.get(country_name = request.POST['addCountry'])

        if add_country:
            user.countries_selected.add(add_country)
            user.countries_not_selected.remove(add_country)

    all_cities = City.objects.filter(country__name='Canada')
    print("CITIES = %s", all_cities)

    return render(request, "getFoods/plan_trip.html", {
        'username' : user.username, 
        'countries_selected' : user.countries_selected,
        'countries_not_selected' : user.countries_not_selected
        })

def itinerary(request):
    return HttpResponse("Hello, world!")

def delete(request, id):
    user = Users.objects.get(username = request.session.get('my_username'))
    country = Countries.objects.get(id = id)
    user.countries_selected.remove(country)
    user.countries_not_selected.add(country)
    return HttpResponseRedirect(reverse('getFoods:plan_trip'))