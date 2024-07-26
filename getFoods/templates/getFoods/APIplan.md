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

	
