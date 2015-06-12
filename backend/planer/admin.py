from django.contrib import admin
from .models import UserSettings, Route, City

# Register your models here.
admin.site.register(UserSettings)
admin.site.register(Route)
admin.site.register(City)