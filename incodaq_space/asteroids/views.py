from django.shortcuts import render
from api_relay.make_requests import fetch_asteroid_location
from incodaq_space.secondary_calculations import api_response_to_string
from .models import asteroids_location_model
import json

# # Creatyour views here.
def asteroid_location_api():
    asteroid_location_api_response = fetch_asteroid_location()
    # save json as string
    asteroid_location_data = api_response_to_string(asteroid_location_api_response)
    test = asteroid_location_data
    # save data to iss_crew model
    asteroids_location_model.objects.create(asteroids_location_json=asteroid_location_data)


def get_asteroid_info():
   try:
      last_asteroid_record = asteroids_location_model.objects.last()
      last_asteroid_record = json.loads(last_asteroid_record.asteroids_location_json)
      #asteroid_data = last_asteroid_record["people"]
      return last_asteroid_record
   except:
      return [{'asteroid_data': "Something went wrong with fetching asteroids #TODO to be moved to celerySS crew data"}]
