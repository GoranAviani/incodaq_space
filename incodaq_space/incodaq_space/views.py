from django.shortcuts import render, redirect
from iss.views import iss_crew_api, iss_location_api
from iss.models import iss_crew_model, iss_location_now_model
import json
#from datetime import datetime, timedelta

def get_iss_crew_info():
   try:
      lastISSCrewDataRec = iss_crew_model.objects.last()
      lastISSCrewDataRec = json.loads(lastISSCrewDataRec.iss_crew_json)
      IssCrewData = lastISSCrewDataRec["people"]
      return IssCrewData
   except:
      return [{'name': "Something went wrong with fetching ISS crew data", "craft": ""}]

def get_iss_location_now_info():
   try:
      lastISSLocationDataRec = iss_location_now_model.objects.last()
      lastISSLocationDataRec = json.loads(lastISSLocationDataRec.iss_location_now_json)
      IssLocationData = lastISSLocationDataRec
      return IssLocationData
   except:
      return [{'name': "Something went wrong with fetching ISS location data", "craft": ""}]

def index(request):

    return render(request,'index.html')


def iss(request):
    iss_crew_api() #TODO to be moved to clery
    iss_location_api()



    iss_crew_info = get_iss_crew_info()
    iss_location_now_info = get_iss_location_now_info()
    print(iss_crew_info)
    print(iss_location_now_info)
    return render(request, 'iss.html',
            {'iss_crew_info': iss_crew_info,
             "iss_location_now_info": iss_location_now_info}
            )
