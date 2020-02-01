from django.shortcuts import render
from api_relay.make_requests import make_iss_api_call
# Create your views here.
def iss_crew_api():
    make_iss_api_call()