from django.db import models
import datetime

# Create your models here.
class asteroids_location_model(models.Model):
    asteroids_location_json = models.CharField(max_length=15000, null=True, blank=True)
    datetime = models.DateTimeField(default=datetime.datetime.utcnow)