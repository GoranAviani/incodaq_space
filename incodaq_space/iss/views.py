from django.shortcuts import render
from api_relay.make_requests import make_iss_api_call
# Create your views here.
from .models import iss_crew_model, iss_location_now_model
import json

def iss_crew_api():
    iss_crew_parameters = {"call_source": "iss_crew_names"}
    iss_iss_crew_api_response = make_iss_api_call(**iss_crew_parameters)
    iss_crew_data = json.dumps(iss_iss_crew_api_response.json()) #save json as string
    #save data to iss_crew model
    iss_crew_model.objects.create(iss_crew_json=iss_crew_data)

def iss_location_api():
    iss_location_parameters = {"call_source": "iss_location_now"}
    iss_location_api_response = make_iss_api_call(**iss_location_parameters)
    iss_locatio_data = json.dumps(iss_location_api_response.json()) #save json as string
    #save data to iss_crew model
    iss_location_now_model.objects.create(iss_location_now_json= iss_locatio_data)