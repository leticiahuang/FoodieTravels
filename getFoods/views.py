from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Countries


# Create your views here.

def index(request):
    return HttpResponse("Please load again.")

def foodPlan(request):

    """if name does not exit:
        create new user
        User.objects.create()
    
    get-user"""

    thisUser = User.objects.get(name=name)


    return render(request, "getFoods/foodPlan.html")

