import geopy.distance
from .models import Cycle, UserCycle
from django.http import JsonResponse
from geopy.geocoders import Nominatim


def calculate_distance(point1, point2):
    return geopy.distance.geodesic(point1, point2)

# def get_position(request):
#     print("thisss")
#     if request.method == 'POST':
#         lat = request.POST.get('lat')
#         lng = request.POST.get('lng')
#         global location
#         location = (lat, lng)
#         return JsonResponse({'status': 'success'})
#     else:
#         print("else")
#         location = (lat, lng)

# def get_position(request):
#     # Get the user's IP address from the request
#     ip_address = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', ''))

#     # Use geopy to determine the user's location based on their IP address
#     geolocator = Nominatim(user_agent="django")
#     location = geolocator.geocode(ip_address)
#     return location


def sort_by_distance(request, user):
    cycles = Cycle.objects.all()
    # location = get_position(request)
    # location = (location.latitude, location.longitude)
    location = (27.6554389,85.320317)
    for cycle in cycles:
        try:
            user_cycle = UserCycle.objects.get(user=user, cycle=cycle)
            user_cycle.distance = calculate_distance(location, cycle.current_location)
            user_cycle.save()
        except UserCycle.DoesNotExist:
            UserCycle.objects.create(user=user, cycle=cycle, distance=calculate_distance(location, cycle.current_location))
    cycles = sorted(cycles, key=lambda x: x.distance)
    return cycles






