from django.shortcuts import render
from api_relay.make_requests import make_iss_api_call
# Create your views here.
from .models import iss_crew_model
def iss_crew_api():
    call_source = {"call_source": "iss_crew_data"}
    iss_crew_data = make_iss_api_call(**call_source)
    print(iss_crew_data)

    #save data to iss_crew model
    iss_crew_model.objects.create(iss_crew_json= iss_crew_data)
