from django.shortcuts import render, redirect
from iss.views import iss_crew_api
from iss.models import iss_crew_model

#from datetime import datetime, timedelta

def get_iss_crew_info():
   result = []
   try:
      lastRec = iss_crew_model.objects.last()

      for x in lastRec.iss_crew_json["people"]:
         result.append({'name': x.name, 'craft': x.craft})
      return result
   except:
      return result

def index(request):

    return render(request,'index.html')


def iss(request):
    iss_crew_api() #TODO to be moved to clery

    iss_crew_info = get_iss_crew_info()
    print(iss_crew_info)
    return render(request, 'iss.html',
            {'iss_crew_info': iss_crew_info,}
            )
