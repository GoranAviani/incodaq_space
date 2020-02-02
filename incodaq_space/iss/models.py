from django.db import models
import datetime
# Create your models here.
#from django.contrib.postgres.fields import JSONField

class iss_crew(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    craft = models.CharField(max_length=50, null=True, blank=True)
    datetime = models.DateTimeField(default=datetime.datetime.utcnow)



class iss_crew_model(models.Model):
    iss_crew_json = models.CharField(max_length=15000, null=True, blank=True)
    datetime = models.DateTimeField(default=datetime.datetime.utcnow)

class iss_location_now_model(models.Model):
    iss_location_now_json = models.CharField(max_length=15000, null=True, blank=True)
    datetime = models.DateTimeField(default=datetime.datetime.utcnow)