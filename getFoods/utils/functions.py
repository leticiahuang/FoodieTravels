import environ
import os
from pathlib import Path

env = environ.Env()
#BASE_DIR = Path(__file__).resolve().parent.parent
#environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

def getMax(arr, prop):
    """
    Used to filter through the Google Maps API results to find resturant
    with highest rating.

    Returns:
        Restaurant object with highest rating. 
    """
    #https://stackoverflow.com/questions/22949597/getting-max-values-in-json-array
    max = None
    restaurant = None
    for i in range(len(arr)):
        if (max is None) or (arr[i][prop] > max):
            max = arr[i][prop]
            restaurant = arr[i]
    return restaurant


GLOBAL_GOOGLE_API_FRONT_KEY = ""
GLOBAL_GOOGLE_API_BACK_KEY = ""

def getGoogleApiKeyBackend():
    global GLOBAL_GOOGLE_API_BACK_KEY
    if GLOBAL_GOOGLE_API_BACK_KEY == "":
        GLOBAL_GOOGLE_API_BACK_KEY = env('GMAP_BACKEND_KEY')
    print("BKKEY ", GLOBAL_GOOGLE_API_BACK_KEY)
    return GLOBAL_GOOGLE_API_BACK_KEY

def getGoogleApiKeyFrontend():
    global GLOBAL_GOOGLE_API_FRONT_KEY
    if GLOBAL_GOOGLE_API_FRONT_KEY == "":
        GLOBAL_GOOGLE_API_FRONT_KEY = env('GMAP_FRONTEND_KEY') 
    print("FEKEY ", GLOBAL_GOOGLE_API_BACK_KEY)
    return GLOBAL_GOOGLE_API_FRONT_KEY