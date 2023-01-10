import requests
import os
import json
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from poster.models import Place, Image


def get_filenames(path):
    filenames = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            filenames.append(filename)
    return filenames


def upload_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    create_new_place(response.json())


def upload_from_path(path):
    filenames = get_filenames(path)
    for filename in filenames:
        with open(os.path.join(path, filename), 'r') as file:
            place_payload = json.load(file)
        create_new_place(place_payload)


def create_images(place_payload, place):
    for num, url in enumerate(place_payload.get('imgs', ''), 1):
        img_filename = f"{num}_{place_payload['title']}.jpg"
        response = requests.get(url)
        response.raise_for_status()
        Image.objects.create(
            picture=ContentFile(response.content, name=img_filename),
            place=place,
        )


def create_new_place(place_payload):
    place, created = Place.objects.get_or_create(
        title=place_payload['title'],
        defaults={
            'description_short': place_payload.get('description_short', ''),
            'description_long': place_payload.get('description_long', ''),
            'lng': place_payload['coordinates']['lng'],
            'lat': place_payload['coordinates']['lat'],
        },
    )
    if created:
        create_images(place_payload, place)
    else:
        print('Объект уже создан')


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--path',
            help='Путь к .json файлу с данными для БД',
        )
        parser.add_argument(
            '--url',
            help='https путь к .json файлу с данными для БД',
        )

    def handle(self, *args, **options):
        path = options['path']
        url = options['url']
        if path:
            upload_from_path(path)
        if url:
            upload_from_url(url)


if __name__ == "__main__":
    Command().handle()
