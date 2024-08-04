def getMax(arr, prop):
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
        file = open("getFoods/secret/google_map_backend_api.key", "r")
        GLOBAL_GOOGLE_API_BACK_KEY = file.read()
        GLOBAL_GOOGLE_API_BACK_KEY = GLOBAL_GOOGLE_API_BACK_KEY.strip()
        file.close() 
    return GLOBAL_GOOGLE_API_BACK_KEY

def getGoogleApiKeyFrontend():
    global GLOBAL_GOOGLE_API_FRONT_KEY
    if GLOBAL_GOOGLE_API_FRONT_KEY == "":
        file = open("getFoods/secret/google_map_frontend_api.key", "r")
        GLOBAL_GOOGLE_API_FRONT_KEY = file.read()
        GLOBAL_GOOGLE_API_FRONT_KEY = GLOBAL_GOOGLE_API_FRONT_KEY.strip()
        file.close() 
    return GLOBAL_GOOGLE_API_FRONT_KEY