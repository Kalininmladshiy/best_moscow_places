from django.shortcuts import render
from .models import Place
from django.urls import reverse


def index(request):
    places = Place.objects.all()
    features = []
    for place in places:
        feature = {
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [place.lng, place.lat]
          },
          "properties": {
            "title": place.title,
            "placeId": place.id,
            "detailsUrl": reverse('places', args=[place.id]),
          }
        }
        features.append(feature)

    places_on_map = {
        'value': {
          "type": "FeatureCollection",
          "features": features,
            }
        }

    return render(request, 'index.html', context=places_on_map)
