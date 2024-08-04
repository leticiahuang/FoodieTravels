
Python/Django
    Lazy-initialization
    View GET VAN/Poutine
        if DB NO has data for VAN/Poutine && the DATA is more than a week {
            fetch from google
            formate the resultsu
            write into DB (table(s)) with timestamp
        }
        do everything above in views.py

        get data from DB about VAN/Poutine <- and then return to html


we are using lazy method. we are making a post request to the google api which will return JSON object. 
Text search wants this as input
curl -X POST -d '{
  "textQuery" : "Spicy Vegetarian Food in Sydney, Australia"
}' \
-H 'Content-Type: application/json' -H 'X-Goog-Api-Key: API_KEY' \
-H 'X-Goog-FieldMask: places.displayName,places.formattedAddress,places.priceLevel' \
'https://places.googleapis.com/v1/places:searchText'

    Non-lazy
    Daemon run once a week
        itarate all possible city
            searhc CTY/Poutine from google
            formating results
            write into DB

    View GET VAN/Poutine
        get data from DB about VAN/Poutine



Create each country’s (name has to be same as Country class) JSON object with 5 top foods


Javascript event listener for click submit
    -> Create new map on Google Maps
    -> Go to backend. Get all cities where user_id in model 1 matches user’s id
	-> Create JSON object for all cities in user's destination with the key values being country, city, food#, food# description. The values are the answer. 
	-> For each city 
        -> Append start of div, then append City name to a string
        -> For each top 5 food of the country from the JSON data
            -> Append name of the food, then description of the food. Then call Maps API to find best restaurant for that food in the city. Append name to description. Add pin on map. 
        ->Append completed map of city (with set radius) to string. Append end of div.
    ->Assign string containing all cities and their foods to innerHTML of itinerary.html 

	
