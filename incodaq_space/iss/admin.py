from django.contrib import admin

# Register your models here.
from .models import iss_crew

class iss_crew_admin (admin.ModelAdmin):
    model = iss_crew
    list_display = ("name", "craft", "datetime")

admin.site.register(iss_crew, iss_crew_admin)