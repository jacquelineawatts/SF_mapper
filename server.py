"""Demonstration of Google Maps."""

from jinja2 import StrictUndefined
from flask import Flask, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, Path
import os
import requests

app = Flask(__name__)
app.secret_key = "temp"
app.jinja_env.undefined = StrictUndefined


#---------------------------------------------------------------------#

@app.route('/')
def index():
    """Show homepage."""

    return render_template("distance.html")


@app.route('/map')
def show_map():
    """Show food trucks from SF Open Data on a map. """

    root_url = 'https://data.sfgov.org/resource/6a9r-agq8.json'
    r = requests.get(root_url)

    food_trucks = {}

    for food_truck in r.json():
        food_trucks[food_truck['applicant']] = {'name': food_truck['applicant'],
                                                'latitude': food_truck['latitude'],
                                                'longitude': food_truck['longitude'],
                                                }     

    print food_trucks

    return render_template('map.html', food_trucks=food_trucks)

@app.route('/get_markers.json')
def get_food_truck_markers():
    """Retrieve API data for food truck lat/long."""

    root_url = 'https://data.sfgov.org/resource/6a9r-agq8.json'
    r = requests.get(root_url)

    food_trucks = { food_truck['applicant']: { 'name': food_truck['applicant'],
                                                'lat': food_truck['latitude'],
                                                'long': food_truck['longitude']
                                              } 
    for food_truck in r.json()[:10]}

    return jsonify(food_trucks)



@app.route('/geolocate')
def geolocate():
    """Show geolocating demo."""

    return render_template("geolocate.html")




#---------------------------------------------------------------------#

if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    DebugToolbarExtension(app)

    app.run(host="127.0.0.1")
