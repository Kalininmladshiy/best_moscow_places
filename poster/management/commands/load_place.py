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


def get_file_content(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.content


def get_json(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def upload_from_url(url):
    place = get_json(url)
    create_new_place(place)


def upload_from_path(path):
    filenames = get_filenames(path)
    for filename in filenames:
        with open(os.path.join(path, filename), 'r') as file:
            place_json = file.read()
        place = json.loads(place_json)
        create_new_place(place)


def create_new_place(place):
    new_place = Place.objects.get_or_create(
        title=place['title'],
        description_short=place['description_short'],
        description_long=place['description_long'],
        lng=place['coordinates']['lng'],
        lat=place['coordinates']['lat'],
     )
    for num, url in enumerate(place['imgs'], 1):
        img_filename = f"{num}_{place['title']}.jpg"
        try:
            img_content = get_file_content(url)
        except requests.exceptions.ConnectionError:
            print('Произошел разрыв сетевого соединения. Ожидаем 10 секунд.')
            time.sleep(10)
            continue
        except requests.exceptions.HTTPError:
            print('Что-то с адресом страницы')
            continue
        img = ContentFile(img_content, name=img_filename)
        new_place[0].images.add(Image.objects.create(picture=img))    


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
