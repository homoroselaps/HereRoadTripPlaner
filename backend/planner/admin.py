from django.contrib import admin
from .models import City, Route, Trip, UserSettings

# Register your models here.
admin.site.register(Route)
admin.site.register(Trip)
admin.site.register(City)
admin.site.register(UserSettings)