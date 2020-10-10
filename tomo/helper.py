from tomo.models import Event, User
from django.db.models import Q
import requests
import json
import pytz

NO_USER = 0

def getEventWithTags(tags):
    ret = Event.objects
    if not tags:
        # if there is no tag
        return ret.all()
    else:
        q = Q()
        for tag in tags:
            # chain filteration
            ret = ret.filter(tags__name__in=[tag])
        return ret.distinct()

def getCurrentUserId(request):
    # if there is session
    if 'user_id' in request.session and request.session['user_id']:
        user_id = request.session['user_id']
        try:
            user = User.objects.get(pk=user_id)
        except:
            return NO_USER
        return request.session['user_id']
    else:
        # default 0 is no user
        return NO_USER

# receive request object, user id
def setUserId(request, user_id=0, username=""):
    if user_id != 0:
        request.session['user_id'] = user_id
    elif username:
        request.session['user_id'] = User.objects.get(username=username).id
    else:
        raise ValueError("Invalid argument: user_id={}\nusername={}".format(user_id, username))

def deleteCookieUserId(request):
    try:
        del request.session['user_id']
    except:
        pass

# find latitude and longtitude using address
def findGeocoding(address):
    API_KEY_GOOGLE = 'AIzaSyCvd_gwQNWo-6oFryV0SML_9xXQFhg7myo'
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + address + '&key=' + API_KEY_GOOGLE
    request = requests.get(url)
    if request.status_code == 200:
        data = json.loads(request.content)
        # return a {'lat': float, 'lng': float} object
        location = data['results'][0]['geometry']['location']
        location['lat'] = float(location['lat'])
        location['lng'] = float(location['lng'])
        print("Location found: ", location)
        return location
    elif request.status_code == 404:
        print('Location not found')
        return {
            'lat': -1,
            'lng': -1
        }
    else:
        print("Error: ", request.content)
        return {
            'lat': -1,
            'lng': -1
        }

def makeAwareDatetime(time):
    return pytz.utc.localize(time)