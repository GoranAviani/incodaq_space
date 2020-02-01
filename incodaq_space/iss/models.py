from django.db import models
import datetime
# Create your models here.

class iss_crew(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    craft = models.CharField(max_length=50, null=True, blank=True)
    datetime = models.DateTimeField(default=datetime.datetime.utcnow)
