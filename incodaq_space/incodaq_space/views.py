from django.shortcuts import render, redirect
from iss.views import iss_crew_api
from iss.models import iss_crew_model
import json
#from datetime import datetime, timedelta

def get_iss_crew_info():
   try:
      lastISSCrewDataRec = iss_crew_model.objects.last()
      lastISSCrewDataRec = json.loads(lastISSCrewDataRec.iss_crew_json)
      IssCrewData = lastISSCrewDataRec["people"]


      return IssCrewData
   except:
      return [{'name': "Something went wrong with fetching crew data", "craft": ""}]

def index(request):

    return render(request,'index.html')


def iss(request):
    #iss_crew_api() #TODO to be moved to clery

    iss_crew_info = get_iss_crew_info()
    print(iss_crew_info)
    return render(request, 'iss.html',
            {'iss_crew_info': iss_crew_info,}
            )
