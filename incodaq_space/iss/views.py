from django.shortcuts import render
from api_relay.make_requests import make_iss_api_call
# Create your views here.
from .models import iss_crew
def iss_crew_api():
    call_source = {"call_source": "iss_crew_data"}
    iss_crew_data = make_iss_api_call(**call_source)
    print(iss_crew_data)

    #save data to iss_crew model
    for x in iss_crew_data["people"]:
        iss_crew.objects.create(name=x["name"], craft=x["craft"])

    #TODO process data from make_iss_api_call?