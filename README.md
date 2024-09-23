# FoodieTravels

#### Summary of Project
This is a website that allows travellers to quickly research local cuisines from every travel destination. First, users must create an account. Then, submit all travel destinations to recieve a tailored guide to local dishes in all cities you will travel to. Each city is accompanies by a Google Maps with top-rated restaurants pinned. 

#### Background
* In the first hackathon I participated in during first year, my team used Django. Only having taken a month of computer science prior, I wasn't able to contribute much in the hackathon. But it inspired me to learn Django which I did this summer. 
* Not only did I learn how to create a full-stack website through Django, I also learned how to write Restful API's, utilize Google Maps API, and obtain a HTTPS domain! I was able to learn and implement tons of technology while creating this website. 

#### Tech Used
* The website is backed by Django and the frontend is developped with HTML, CSS, and JavaScript. 
* User data and restaurant data is cached/stored in SQLite. 
* RESTful API is used to communicate between the backend and front end.
* The website is hosted on AWS on an EC2 instance and the domain is managed by Route 53 and Nginx. 
* Traffic to the site is managed with GUnicorn through wsgi. 
* The SSL certifcate was obtained through certbot. 
* Google Maps Places API is used to search for top rated restaurants. It is called if the database does not contain information for that city. It is also called it find restaurants if the last search is over six weeks old. 
* Google Maps JavaScript API is used to display Maps for the frontend.
* Created separate configurations for development and production environments  
* Utilized GUnicorn for 3rd party HTTP server through wsgi and socket a socket file.