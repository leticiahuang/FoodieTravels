from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Users, Food
import logging
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  
from .forms import RegisterForm  
from cities_light.models import Country, City
from django.http import JsonResponse
from django.core.serializers import serialize
import json


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


#SECTION FOR PLAN_TRIP.HTML

def plan_trip(request):
    user = Users.objects.get(username = request.session.get('my_username'))
    
    #if new country submitted, add
    if request.method == "POST":
        #check for both city and country name in case of duplicate city names
        new_dest = City.objects.get(name = request.POST['add-city'], country__name = request.POST['add-country'])
        #don't need to check if new_dest already in user.destination, django doesn't allow
        user.destinations.add(new_dest)

    return render(request, "getFoods/plan_trip.html", {
        'user' : user,
        'countries' : Country.objects.all(),
        'cities' : City.objects.all(),
        })

def delete(request, id):
    #this view used to delete a destination from user.destinations
    user = Users.objects.get(username = request.session.get('my_username'))
    destination = user.destinations.get(id = id)
    user.destinations.remove(destination)
    return HttpResponseRedirect(reverse('getFoods:plan_trip'))

def get_cities(request, country):
    #this view used to filter cities depending on country chosen
    query_results = City.objects.filter(country__name = country)
    #fields specify which fields of the model to return
    #serialize creates json object, don't need to return JsonResponse or will be changed twice
    json_object = serialize("json", query_results, fields=['name']) 
    return HttpResponse(json_object, content_type="application/json")

    
    #logger.info("----- JSON: %s", json_object)
    


#SECTION FOR ITINERARY.HTML

def itinerary(request):
    user = Users.objects.get(username = request.session.get('my_username'))
    return render(request, "getFoods/itinerary.html", {
        'user' : user,
        })

def get_top_foods(request):
    user = Users.objects.get(username = request.session.get('my_username'))
    #https://javaee.github.io/tutorial/jsonp001.html
    #outer layer is a list so we can treat json as list later
    all_dest = []
    for city in user.destinations.all():
        city_all_food = []
        country = Country.objects.get(name = city.country.name)
        top_foods = Food.objects.filter(country_id = country.id)
    
        for curr_food in top_foods:
            curr_food_dict = {
                "city_name" : city.name,
                "city_id" : city.id,
                "food_name" : curr_food.name,
                "food_descr" : curr_food.descr,
            }
            city_all_food.append(curr_food_dict)
            #city_all_food[curr_food.name] = curr_food_dict
    
        all_dest.append(city_all_food)
        #all_dest[city.name] = city_all_food
        
    json_object = json.dumps(all_dest, indent=5)
    #since all_dest already serialized by json.dumps, don't need to return JsonResponse
    return HttpResponse(json_object, content_type="application/json")
    
    #logger.info("----- JSON: %s", json_object)
