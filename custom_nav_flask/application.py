from flask import Flask, request, render_template
from flask_json import FlaskJSON, JsonError, json_response
import os
import requests
from flask_cors import CORS
import json

# local imports
from height_logic import get_low_clearances, get_med_coordinate, haversine, km_to_mile, haversine, location_finder

application = app = Flask(__name__)
FlaskJSON(app)
cors = CORS(app)



@app.route('/')
def root():
    """
    Testing
    """
    return "Test Successful"


@app.route('/fetch_low_clearance', methods=['POST'])
def fetch_walmart():
  """
  API route that receives user information and returns relevant routing datapoints
  """

  data = request.get_json(force=True)

  user_height = data['height']
  lon1 = data['start_lon']
  lat1 = data['start_lat']
  lon2 = data['end_lon']
  lat2 = data['end_lat']

  lat_med, lon_med = get_med_coordinate(lon1, lat1, lon2, lat2)
  distance = km_to_mile(haversine(lon1, lat1, lon2, lat2))
  df = get_low_clearances(user_height)
  df = location_finder(df, lat_med, lon_med, distance)

  return df.to_json(orient='records')

if __name__ == '__main__':
        application.run()


