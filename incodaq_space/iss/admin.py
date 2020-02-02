from django.contrib import admin

# Register your models here.
from .models import iss_crew_model, iss_location_now_model

class iss_crew_model_admin (admin.ModelAdmin):
    model = iss_crew_model
    list_display = ("iss_crew_json")

admin.site.register(iss_crew_model)


class iss_location_now_model_admin (admin.ModelAdmin):
    model = iss_location_now_model
    list_display = ("iss_location_now_json")

admin.site.register(iss_location_now_model)