from django.shortcuts import render
from api_relay.make_requests import make_iss_api_call
# Create your views here.
from .models import iss_crew_model, iss_location_now_model
import json
from incodaq_space.incodaq_space.logging_is import api_errors

def iss_crew_api():
    callSource = {"call_source": "iss_crew_names"}
    issCrewDataStatus, issCrewDataResult = make_iss_api_call(**callSource)
    if issCrewDataStatus == "error":
        api_errors.error("{}" .format(issCrewDataResult))
    else:
        issCrewDataString = json.dumps(issCrewDataResult) #save json as string

        #save data to iss_crew model
        iss_crew_model.objects.create(iss_crew_json=issCrewDataString)

def iss_location_api():
    callSource = {"call_source": "iss_location_now"}
    issLocationNowStatus, issLocationNowResult = make_iss_api_call(**callSource)
    if issLocationNowStatus == "error":
        #TODO log error here, save type of error
        pass
    else:
        issLocationNowString = json.dumps(issLocationNowResult) #save json as string
        #save data to iss_crew model
        iss_location_now_model.objects.create(iss_location_now_json= issLocationNowString)