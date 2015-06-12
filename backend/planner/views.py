import json
from urllib.request import urlopen
from django.http import HttpResponse

# Create your views here.
appId = '?app_id=XICryEiu3MwGTqoBqx8S'
appCode = '&app_code=sEZSFHpqGqWcGX4gmWixlQ'

geocoder = 'http://reverse.geocoder.cit.api.here.com/6.2/reversegeocode.json' + appId + appCode
geocoderSuffix = '&mode=retrieveAreas&gen=8&addressattributes=city&locationattributes=ad&level=city&maxresults=20'

routeCalc = 'http://route.cit.api.here.com/routing/7.2/calculateroute.json' + appId + appCode
routeCalcSuffix = '&routeattributes=sh,ri&mode=fastest;car;&resolution=92'

#routeInfo = 'http://route.cit.api.here.com/routing/7.2/getroute.json' + appId + appCode
#routeInfoSuffix = '&mode=fastest;car;&resolution=92'

def index(request, x1, y1, x2, y2, time):
    timeToTarget = int(time) + 1
    cycles = 0
    cC = [int(x2), int(y2)]
    cities = []
    names = []
    while timeToTarget > int(time) and cycles < 10:
        cC = [(cC[0] + int(x2)) / 2, (cC[1] + int(y2)) / 2]
        cycles += 1
        url = routeCalc + '&waypoint0=geo!' + x1 + ',' + y1 + '&waypoint1=geo!' + str(cC[0]) + ',' + str(cC[1]) + routeCalcSuffix
        jsonResponse = json.loads(urlopen(url).read().decode('utf-8'))
        #routeID = json['Response']['Route']['RouteId']
        #url = routeInfo + '&routeId=' + routeID + routeInfoSuffix
        #json = json.load(urlopen(url).read().decode('utf-8'))
        timeToTarget = jsonResponse['response']['route'][0]['leg'][0]['maneuver'][0]['travelTime']

    url = geocoder + '?prox=' + str(cC[0]) + ',' + str(cC[1]) + ',20000' + geocoderSuffix
    jsonResponse = json.loads(urlopen(url).read().decode('utf-8'))
    for result in jsonResponse['response']['view']['result']:
        name = result['location']['address']['city']
        coords = result['location']['displayPosition']
        if name not in names:
            names += names
            coords += cities

    return HttpResponse(cities)