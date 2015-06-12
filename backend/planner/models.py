from django.db import models

# Create your models here.
class UserSettings(models.Model):
    maxDrivingPerDay = models.IntegerField('inHours')
    totalDays = models.IntegerField()

class Route(models.Model):
    session = models.IntegerField()

class City(models.Model):
    name = models.CharField(max_length=40)
    x_coord = models.FloatField()
    y_coord = models.FloatField()
    def __str__(self):
        return self.name

class Trip(models.Model):
    city = models.ForeignKey(City)
    time = models.FloatField()
    route = models.ForeignKey(Route)
    def __str__(self):
        return self.startCity.name