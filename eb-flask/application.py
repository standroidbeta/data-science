from flask import Flask, request, render_template
from flask_json import FlaskJSON, JsonError, json_response
import os
import requests
from flask_cors import CORS
import json

#local imports
from poi import location_finder

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

@app.route('/fetch_data', methods=['POST'])
def fetch_data():
  """
  API route that receives user information and returns relevant routing datapoints and places of interest
  """

  data = request.get_json(force=True)

  user_lat = data['latitude'] 
  user_long = data['longitude']
  user_dist = data['distance']

  rest_df = location_finder(lat=user_lat, long=user_long, dist=user_dist)          

  #return json_response()
# 

  return json_response(latitude = rest_df['Latitude'], longitude = rest_df['Longitude'],
                       state=rest_df['State'], roadway=rest_df['Roadway'],
                       direction=rest_df['Direction'], name=rest_df['Name'],
                       mile_marker = rest_df['Mile Marker'], restrooms = rest_df['Restrooms'],
                       picnic_tables=rest_df['Picnic Tables'], vending_machines=rest_df['Vending Machines'],
                       pets=rest_df['Pet Walking Area'], handicapable=rest_df['Handicapped Facilities'],
                       rv_dump=rest_df['RV Dump'], restaurant=rest_df['Restaurant'], gas=rest_df['Gas'],
                       scenic=rest_df['Scenic View'])

  
if __name__ == '__main__':
        application.run()