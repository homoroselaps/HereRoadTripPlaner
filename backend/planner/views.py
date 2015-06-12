import json
from urllib.request import urlopen
from django.http import HttpResponse

# Create your views here.
appId = '?app_id=XICryEiu3MwGTqoBqx8S'
appCode = '&app_code=sEZSFHpqGqWcGX4gmWixlQ'

geocoder = 'https://reverse.geocoder.cit.api.here.com/6.2/reversegeocode.json' + appId + appCode
geocoderSuffix = '&mode=retrieveAreas&gen=8&addressattributes=city&locationattributes=ad&level=city&maxresults=20'

routeCalc = 'https://route.cit.api.here.com/routing/7.2/calculateroute.json' + appId + appCode
routeCalcSuffix = '&routeattributes=sh,ri&mode=fastest;car;&resolution=92'

#routeInfo = 'http://route.cit.api.here.com/routing/7.2/getroute.json' + appId + appCode
#routeInfoSuffix = '&mode=fastest;car;&resolution=92'

def index(request, x1, y1, x2, y2, time):
    timeToTarget = time + 1
    cycles = 0
    cC = [x2, y2]
    cities = []
    names = []
    while not (timeToTarget < time) and cycles < 10:
        cC = [(cC[0] + x2) / 2, (cC[1] + y2) / 2]
        cycles += 1
        url = routeCalc + '&waypoint0=geo!' + x1 + ',' + y1 + '&waypoint1=geo!' + cC[0] + ',' + cC[1] + routeCalcSuffix
        json = json.load(urlopen(url).read().decode('utf-8'))
        #routeID = json['Response']['Route']['RouteId']
        #url = routeInfo + '&routeId=' + routeID + routeInfoSuffix
        #json = json.load(urlopen(url).read().decode('utf-8'))
        timeToTarget = json['Response']['Route']['Leg']['Maneuver']['TravelTime']

    url = geocoder + '?prox=' + cC[0] + ',' + cC[1] + ',20000' + geocoderSuffix
    json = json.load(urlopen(url).read().decode('utf-8'))
    for result in json['Response']['View']['Result']:
        name = result['Location']['Address']['City']
        coords = result['Location']['DisplayPosition']
        if name not in names:
            names += names
            coords += cities

    return HttpResponse(cities)