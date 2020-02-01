from django.shortcuts import render, redirect
from iss.views import iss_crew_api

def index(request):

    return render(request,'index.html')


def iss(request):
    iss_crew_api()
    return render(request, 'iss.html')
