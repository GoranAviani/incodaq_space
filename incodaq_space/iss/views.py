from django.shortcuts import render
from api_relay.make_requests import fetch_iss_crew_names, fetch_iss_location, fetch_asteroid_location
# Create your views here.
from .models import iss_crew_model, iss_location_now_model
from incodaq_space.incodaq_space.asteroids.models import asteroids_location_model
import json

def api_response_to_string(api_response):
    return json.dumps(api_response.json())

def iss_crew_api():
    iss_iss_crew_api_response = fetch_iss_crew_names()
    # save json as string
    iss_crew_data = api_response_to_string(iss_iss_crew_api_response)
    #save data to iss_crew model
    iss_crew_model.objects.create(iss_crew_json=iss_crew_data)

def iss_location_api():
    iss_location_api_response = fetch_iss_location()
    # save json as string
    iss_locatio_data = api_response_to_string(iss_location_api_response)
    #save data to iss_crew model
    iss_location_now_model.objects.create(iss_location_now_json=iss_locatio_data)

def asteroid_location_api():
    asteroid_location_api_response = fetch_asteroid_location()
    # save json as string
    asteroid_location_data = api_response_to_string(asteroid_location_api_response)
    test = asteroid_location_data
    # save data to iss_crew model
    asteroids_location_model.objects.create(asteroids_location_json=asteroid_location_data)