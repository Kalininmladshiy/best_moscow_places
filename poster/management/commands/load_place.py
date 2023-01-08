import requests
import os
import time
import json
from pathlib import Path
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
            place_json = file.read()
        place_payload = json.loads(place_json)
        create_new_place(place_payload)


def create_images(place_payload):
    images = []
    for num, url in enumerate(place_payload['imgs'], 1):
        img_filename = f"{num}_{place_payload['title']}.jpg"
        try:
            response = requests.get(url)
            response.raise_for_status()
            img_content = response.content
        except requests.exceptions.ConnectionError:
            print('Произошел разрыв сетевого соединения. Ожидаем 10 секунд.')
            time.sleep(10)
            continue
        except requests.exceptions.HTTPError as e:
            print(e)
            continue
        img = Image.objects.create(
            picture=ContentFile(img_content, name=img_filename)
        )
        images.append(img)
    return images


def create_new_place(place_payload):
    place, created = Place.objects.get_or_create(
        title=place_payload['title'],
        defaults={
            'description_short': place_payload['description_short'],
            'description_long': place_payload['description_long'],
            'lng': place_payload['coordinates']['lng'],
            'lat': place_payload['coordinates']['lat'],
        },
    )
    if created:
        images = create_images(place_payload)
        for img in images:
            place.images.add(img)
    else:
        print('Объект уже создан')


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--path',
            default=Path.cwd() / 'static' / 'places',
            help='Путь к .json файлу с данными для БД',
        )
        parser.add_argument(
            '--url',
            help='https путь к .json файлу с данными для БД',
        )

    def handle(self, *args, **options):
        path = options['path']
        url = options['url']
        upload_from_path(path)
        if url:
            upload_from_url(url)


if __name__ == "__main__":
    Command().handle()
