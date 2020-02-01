from django.shortcuts import render
from api_relay.make_requests import make_iss_api_call
# Create your views here.

def iss_crew_api():
    call_source = {"call_source": "iss_crew_data"}
    iss_crew_data = make_iss_api_call(**call_source)
    print(iss_crew_data)
    #TODO process data from make_iss_api_call?