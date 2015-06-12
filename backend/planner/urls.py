from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'\?(?P<x1>\d+\.?\d*)&(?P<y1>\d+\.?\d*)&(?P<x2>\d+\.?\d*)&(?P<y2>\d+\.?\d*)&(?P<time>[1]?[1-9])$',
        views.index, name='index')
]