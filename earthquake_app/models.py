from django.db import models

class Event(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    magnitude = models.FloatField()
    depth = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
