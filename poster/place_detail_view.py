from django.shortcuts import get_object_or_404
from django.http.response import JsonResponse
from .models import Place


def get_place(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_info = {
        'title': place.title,
        'imgs': [image.picture.url for image in place.images.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lng': place.lng,
            }
        }

    return JsonResponse(
        place_info,
        json_dumps_params={'ensure_ascii': False, 'indent': 2}
        )
