from django.shortcuts import render
from api_relay.make_requests import retrieve_iss_crew_names, retrieve_iss_location_now
# Create your views here.
from .models import iss_crew_model, iss_location_now_model
import json

def iss_crew_api():
    iss_iss_crew_api_response = retrieve_iss_crew_names()
    iss_crew_data = json.dumps(iss_iss_crew_api_response.json()) #save json as string
    #save data to iss_crew model
    iss_crew_model.objects.create(iss_crew_json=iss_crew_data)

def iss_location_api():
    iss_location_api_response = retrieve_iss_location_now()
    iss_locatio_data = json.dumps(iss_location_api_response.json()) #save json as string
    #save data to iss_crew model
    iss_location_now_model.objects.create(iss_location_now_json= iss_locatio_data)