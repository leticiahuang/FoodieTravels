from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Users, Food
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  
from .forms import RegisterForm  
from cities_light.models import Country, City
from .utils.functions import getGoogleApiKeyFrontend
 #logger.info("----- info: %s", value)





def index(request):
    return HttpResponseRedirect(reverse('getFoods:login'))




def register(request):
    """
    If user's first time to site (GET), renders registration page.
    Else (POST), uses the info user inputted to create and register new user. 
    """

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        #if valid, create user and redirect to login 
        if form.is_valid():
            #creates user for django admin
            form.save() 
            #create user for Users model
            username = form.cleaned_data.get('username') 
            user = Users.objects.create(username = username)
            messages.success(request, "Account created.")
            return HttpResponseRedirect(reverse('getFoods:login'))
        #if not valid, go to register page again with same form
        else:
            messages.error(request, "Please change inputs and try again.")
            return render(request, "getFoods/register.html", {
                    'RegisterForm': form})
    
    #Else create new form and get user to register
    form = RegisterForm()
    return render(request, "getFoods/register.html", {'RegisterForm': form})




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)

        if user: 
            login(request, user)
            #set session cookie
            request.session['my_username'] = username
            return HttpResponseRedirect(reverse('getFoods:plan_trip'))
        else:
            return render(request, "getFoods/login.html",
                {'message': "Wrong username or password."})

    #go to login page if new to site
    return render(request, "getFoods/login.html")




def logout_view(request):
    logout(request)
    try:
        del request.session['username']
    except KeyError:
        pass
    return render(request, "getFoods/login.html", {'message': "Logged out."})




#SECTION FOR PLAN_TRIP.HTML

def plan_trip(request):
    """
    If POST, it means new country is submitted, add the country.
    Else, it is the user's first time on the page so direct them to html. 
    """

    user = Users.objects.get(username = request.session.get('my_username'))

    if request.method == "POST":
        #check for both city and country name in case of duplicate city names
        new_dest = City.objects.get(name = request.POST['add-city'], 
            country__name = request.POST['add-country'])
        #don't check if new_dest exists in user.destination, django checks
        user.destinations.add(new_dest)

    return render(request, "getFoods/plan_trip.html", {
        'user': user,
        'countries': Country.objects.all(),
        'cities': City.objects.all(),
        })




def delete(request, id):
    """
    Delete destination from user.destinations.
    """

    user = Users.objects.get(username = request.session.get('my_username'))
    destination = user.destinations.get(id = id)
    user.destinations.remove(destination)
    return HttpResponseRedirect(reverse('getFoods:plan_trip'))

    
    

#SECTION FOR ITINERARY.HTML

def itinerary(request):
    """
    Leads user to Itinerary page after submitting Plan Trip page.
    """

    user = Users.objects.get(username = request.session.get('my_username'))
    gmap_frontend_key = getGoogleApiKeyFrontend()
    return render(request, "getFoods/itinerary.html", {
        'user': user,
        'frontend_api_key': gmap_frontend_key
        })





   

