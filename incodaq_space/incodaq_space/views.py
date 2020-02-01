from django.shortcuts import render, redirect
from incodaq_space.iss.views import iss_crew_api

def index(request):
    iss_crew_api()
    return render(request,'index.html')
