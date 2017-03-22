# NextGenVest
Create a REST API that determines maximum scholarship amount

# Resources and Actions
URL                 METHOD        OPERATION
/                   GET           displays data from psuedo-database
/max_scholarship    GET           displays max_scholarship
/max_scholarship    POST          runs algorithm, posts to max_scholarship

# Required
- Numpy ( pip install numpy )
- Flask ( pip install flask )
- curl (or any POST handler)

# Build Instructions
- Clone the repo
- Edit the scholarships.py file and enter the lists of lists into data, or generate random via numpy
- Run flask
    1. $ export FLASK_APP=scholarships.py
    2. $ flask run
- open a second window in the terminal
- use curl for GET request
    1. $ curl -i http://localhost:5000/ (to see data)
    2. $ curl -i http://localhost:5000/max_scholarship (to see output)
- use curl for POST request
    1. $ curl -i -H "Content-Type: application/json" -X POST http://localhost:5000/max_scholarship

# Notes
I emailed Will, but I never received a response. I wasn't 100% sure how to handle the GET request namely because I wasn't sure how you were interacting with my code. Due to time constraints I just chose a direct (albeit ugly) method because I needed to begin the process. Whomever is looking through the code essentially puts the lists into my pseudo-database. I make GET requests to the "database", then everything goes from there. 

# Back-End Challenge Description
how to make your api downloadable
Lucky you! Your hacking skills have been recognized and you've been awarded a bunch of scholarships (woot!). The catch is that you can only pick 11 scholarships...

In this challenge, pick the 11 scholarships that give you the most money! You can only pick sequential scholarships and the product of all scholarships you pick is how much money you'll be awarded! (this school is very cheap, so you only need a few dollars... scholarships are in the range 0-100).

API Specs:
POST /max_scholarship
'Content-Type: application/json'

Sample json:

{"data": [[1,2,3,4,5], [1,1,2,3,5], [3,4,5,5,5], [3,4,5,9,5], [1,1,5,5,25]]}

Response:

{"sequence": [5,9,25], "total": 1125}


