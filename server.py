"""Demonstration of Google Maps."""

from jinja2 import StrictUndefined
from flask import Flask, render_template, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, Path
import os

app = Flask(__name__)
app.secret_key = "temp"
app.jinja_env.undefined = StrictUndefined

#---------------------------------------------------------------------#

@app.route('/')
def index():
    """Show homepage."""

    google_api_key = os.environ['GOOGLE_MAP_API_KEY']

    return render_template("map.html", google_api_key=google_api_key)


# @app.route('/bears.json')
# def bear_info():
#     """JSON information about bears."""

#     bears = {
#         bear.marker_id: {
#             "bearId": bear.bear_id,
#             "gender": bear.gender,
#             "birthYear": bear.birth_year,
#             "capYear": bear.cap_year,
#             "capLat": bear.cap_lat,
#             "capLong": bear.cap_long,
#             "collared": bear.collared.lower()
#         }
#         for bear in Bear.query.limit(50)}

#     return jsonify(bears)


# @app.route('/simplemap')
# def simple():
#     """Show simple map."""

#     return render_template("simple.html")


# @app.route('/geolocate')
# def geolocate():
#     """Show geolocating demo."""

#     return render_template("geolocate.html")


# @app.route('/savemap')
# def save():
#     """Saving demo."""

#     return render_template("saved.html")


#---------------------------------------------------------------------#

if __name__ == "__main__":
    app.debug = True
    connect_to_db(app)
    DebugToolbarExtension(app)

    app.run(host="127.0.0.1")
