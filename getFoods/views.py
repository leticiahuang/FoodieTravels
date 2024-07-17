from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Users, Countries
import logging
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm  
from .forms import RegisterForm  


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
            user = form.save() 

            #create user for Users model
            new_country_list = Countries()
            Users(username = request.POST['username']).save()
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
        request.session['username'] = username
        request.session['password'] = password

        user = authenticate(request, username = username, password = password)

        #if user exists, login
        if user: 
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
                return HttpResponse("You're logged in.")
            else:
                return HttpResponse("Please enable cookies and try again.")
            login(request, user)
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
    user = Users.objects.get(username='leticia')
    countries_selected = user.countries_selected.all()
    countries_not_selected = Countries.objects.raw("SELECT * FROM getFoods_countries WHERE NOT EXISTS (select countries_id from getFoods_users_countries_selected WHERE getFoods_countries.id=getFoods_users_countries_selected.countries_id)")
    
    #if new country submitted, add
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            addCountry = form.cleaned_data['addCountry']
            deleteCountry = form.cleaned_data['deleteCountry']

        if addCountry:
            countries_selected.add(Countries.objects.get(country_name = addCountry))
        if deleteCountry:
            countries_selected.delete(Countries.objects.get(country_name = deleteCountry))
    
    return render(request, "getFoods/plan_trip.html", {
        'user' : user, 
        'countries_selected' : countries_selected,
        'countries_not_selected' : countries_not_selected
        })

def itinerary(request):
    return HttpResponse("Hello, world!")