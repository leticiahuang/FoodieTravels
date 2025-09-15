from cities_light.models import Country, City
from .models import Users, Food, Restaurant
from django.core.serializers import serialize
from datetime import datetime, timedelta
from .utils.functions import getMax, getGoogleApiKeyBackend, getGoogleApiKeyFrontend
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import pytz
import requests
import logging
import json




def get_cities(request, country):
    """
    API called from plan_trip.html when a country is chosen in drop down list. 
    Filters through all cities to return only the country's cities.

    Returns: 
        JSON obejct of Country.city

    Note: serialize() creates json object, don't use JsonResponse or will be 
    serialized twice. Createing JSON object with serialize() and not 
    JsonResponse because query_results is not in dict format -> error. 
    """

    query_results = City.objects.filter(country__name = country)
    #fields specify which fields of the model to use for json object
    json_object = serialize("json", query_results, fields=('name', 'id')) 
    return HttpResponse(json_object, content_type="application/json")




def get_top_foods(request):
    """
    An API called from itinerary.html that retrieves restaurant info for the 
    top 5 foods of user's destinations. Calls Google Maps API (text search) 
    to find restaurant info if not already in DB.
    
    Returns:
        JSON object of structure [city:[food:[resto info]]]


    Help from https://javaee.github.io/tutorial/jsonp001.html 
    """

    user = Users.objects.get(username = request.session.get('my_username'))

    utc=pytz.UTC
    now = utc.localize(datetime.now())
    
    all_dest = []
    #create dictionary for every city in user's destinations
    for city in user.destinations.all():
        city_all_food = []
        country = Country.objects.get(name = city.country.name)
        top_foods = Food.objects.filter(country_id = country.id)
        
        #create dictionary for every food in the city
        for curr_food in top_foods:
            resto = get_resto(curr_food, city, now)

            #create dict to turn into json response
            curr_food_dict = {
                "city_name": city.name,
                "city_id": city.id,
                "display_name": curr_food.display_name,
                "food_descr": curr_food.descr,
                "resto_name": resto.resto_name,
                "resto_latitude": resto.resto_latitude,
                "resto_longitude": resto.resto_longitude
            }
            city_all_food.append(curr_food_dict)

        all_dest.append(city_all_food)

    #create and return json object    
    json_object = json.dumps(all_dest, indent=5)
    return HttpResponse(json_object, content_type="application/json")




def get_resto(curr_food, city, now):
    """
    A function that returns restaurant from DB. If resto hasn't been initialized
     or data is old, call API. Used by get_resto().
    
    Returns:
        restaurant object from DB
    """

    #do_reload: if results are expired and need to recall api for resturant db
    do_reload = True 

    if Restaurant.objects.filter(city = city, food_name = curr_food).exists():
        resto = Restaurant.objects.get(city=city, food_name=curr_food)
        record_time = resto.updated_at
        if now - record_time > timedelta(days=60):
            # Delete old resto and get new one if expired
            resto.delete()
            resto = call_gmap(curr_food, city)
            resto.save()

    else:
        #call GMAP api to get find best restaurant if data DNE or expired
        resto = call_gmap(curr_food, city)
        resto.save()

    return resto




def call_gmap(curr_food, city):
    """
    A function that calls Google Maps Text Search API and filters results
    for best restaurant. Used by get_resto().
    
    Returns:
        restaurant object from GMaps API
    """

    gmap_url = "https://places.googleapis.com/v1/places:searchText"
    gmap_backend_key = getGoogleApiKeyBackend()
    gmap_headers = {
        'Content-Type': 'application/json',
        'X-Goog-Api-Key': gmap_backend_key,
        'X-Goog-FieldMask': 
            'places.displayName,places.userRatingCount,places.location'
    }   

    gmap_request_data = {
        'textQuery': f"best {curr_food.search_name} in {city}",
        'minRating': 4,
    }

    gmap_response = requests.post(gmap_url, headers=gmap_headers, 
        json=gmap_request_data)

    #if api call success, filter for best resto and save to DB
    if gmap_response.status_code == 200:
        gmap_json = gmap_response.json()
        if 'places' not in gmap_json:
            resto = Restaurant(
            city = city,
            food_name = curr_food,
            resto_name = f"Unfortunately we couldn't find any restaurants in {city.name}",
            resto_latitude = 90,
            resto_longitude = 0, 
            updated_at = datetime.now()
        )
            # messages.info('Sorry, { city } is too small, please remove.')
            # return JsonResponse(["msg", "....", 1], safe=False);
        else :
            best_resto = getMax(gmap_json['places'], 'userRatingCount')
            resto = Restaurant(
                city = city,
                food_name = curr_food,
                resto_name = best_resto['displayName']['text'],
                resto_latitude = best_resto['location']['latitude'],
                resto_longitude = best_resto['location']['longitude'], 
                updated_at = datetime.now()
            )
        return resto

    else:
        return render("Internal error, try again.")
    


