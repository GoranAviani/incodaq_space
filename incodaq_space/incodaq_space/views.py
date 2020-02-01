from django.shortcuts import render, redirect
from iss.views import iss_crew_api
from iss.models import iss_crew

def get_iss_crew_info():
   result = []
   try:
      foundISSCrew = iss_crew.objects.all()
      for x in foundISSCrew:
         # {'city': city, 'temp': processedTemp, 'iconDesc': processedIconText}
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
    return render(request, 'iss.html')
