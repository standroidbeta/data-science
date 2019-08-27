from flask import Flask, request, render_template
from flask_json import FlaskJSON, JsonError, json_response
import os
import requests
from flask_cors import CORS
import json

#local imports
from poi import location_finder
from poi import df_rest, df_walmart, df_weigh, df_descents, df_tourist, df_campsite, df_dump

# Elastic Beanstalk initalization
application = app = Flask(__name__)
FlaskJSON(app)
cors = CORS(app)

@app.route('/')
def root():
    """
    Testing
    """
    return "Test Successful"

@app.route('/fetch_walmart', methods=['POST'])
def fetch_walmart():
  """
  API route that receives user information and returns relevant routing datapoints and places of interest
  """

  data = request.get_json(force=True)

  user_lat = data['latitude'] 
  user_long = data['longitude']
  user_dist = data['distance']

  final_df = location_finder(df = df_walmart, latitude=user_lat, longitude=user_long, distance=user_dist)          

  return final_df.to_json(orient='records')

@app.route('/fetch_rest_area', methods=['POST'])
def fetch_rest_area():
  """
  API route that receives user information and returns relevant routing datapoints and places of interest
  """

  data = request.get_json(force=True)

  user_lat = data['latitude'] 
  user_long = data['longitude']
  user_dist = data['distance']

  final_df = location_finder(df = df_rest, latitude=user_lat, longitude=user_long, distance=user_dist)          

  return final_df.to_json(orient='records')

@app.route('/fetch_weigh_station', methods=['POST'])
def fetch_weigh_station():
  """
  API route that receives user information and returns relevant routing datapoints and places of interest
  """

  data = request.get_json(force=True)

  user_lat = data['latitude'] 
  user_long = data['longitude']
  user_dist = data['distance']

  final_df = location_finder(df = df_weigh, latitude=user_lat, longitude=user_long, distance=user_dist)          

  return final_df.to_json(orient='records')

@app.route('/fetch_road_descents', methods=['POST'])
def fetch_road_descents():
  """
  API route that receives user information and returns relevant routing datapoints and places of interest
  """

  data = request.get_json(force=True)

  user_lat = data['latitude'] 
  user_long = data['longitude']
  user_dist = data['distance']

  final_df = location_finder(df = df_descents, latitude=user_lat, longitude=user_long, distance=user_dist)          

  return final_df.to_json(orient='records')

@app.route('/fetch_tourist_sites', methods=['POST'])
def fetch_tourist_sites():
  """
  API route that receives user information and returns relevant routing datapoints and places of interest
  """

  data = request.get_json(force=True)

  user_lat = data['latitude'] 
  user_long = data['longitude']
  user_dist = data['distance']

  final_df = location_finder(df = df_tourist, latitude=user_lat, longitude=user_long, distance=user_dist)          

  return final_df.to_json(orient='records')

@app.route('/fetch_campsite', methods=['POST'])
def fetch_campsite():
  """
  API route that receives user information and returns relevant routing datapoints and places of interest
  """

  data = request.get_json(force=True)

  user_lat = data['latitude'] 
  user_long = data['longitude']
  user_dist = data['distance']

  final_df = location_finder(df = df_campsite, latitude=user_lat, longitude=user_long, distance=user_dist)          

  return final_df.to_json(orient='records')

@app.route('/fetch_dump_station', methods=['POST'])
def fetch_dump_station():
  """
  API route that receives user information and returns relevant routing datapoints and places of interest
  """

  data = request.get_json(force=True)

  user_lat = data['latitude'] 
  user_long = data['longitude']
  user_dist = data['distance']

  final_df = location_finder(df = df_dump, latitude=user_lat, longitude=user_long, distance=user_dist)          

  return final_df.to_json(orient='records')

if __name__ == '__main__':
        application.run()