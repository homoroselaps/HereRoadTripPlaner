from django.db import models

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=40)
    x = models.IntegerField('Coordinate X')
    y = models.IntegerField('Coordinate Y')
    def __str__(self):
        return self.name

class UserSettings(models.Model):
    sessionId = models.IntegerField()
    drivingPerDay = models.IntegerField('in hours')
    totalDays = models.IntegerField()
    def __str__(self):
        return self.sessionId

class Route(models.Model):
    city = models.ForeignKey(City)
    settings = models.ForeignKey(UserSettings)
    def __str__(self):
        return self.city

