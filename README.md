# best_moscow_places
Данный репозиторий представляет собой сайт о самых интересных местах в Москве.
![image](https://user-images.githubusercontent.com/106922768/205290329-68dca9ac-592c-4c55-a25a-4a547f4cb00c.png)
    
[Демонстрация сайта](http://maksim220785.pythonanywhere.com/)
## Установка:

### 1. Копируем содержимое проекта себе в рабочую директорию

### 2. Разворачиваем внутри скопированного проекта виртуальное окружение:
```
python -m venv <название виртуального окружения>
```

### 3. Устанавливаем библиотеки:
```
pip install -r requirements.txt
```

### 4. Для хранения переменных окружения создаем файл .env:
```
touch .env
```
Генерируем секретный ключ DJANGO в интерактивном режиме python:
* `python`
* `import django`
* `from django.core.management.utils import get_random_secret_key`
* `print(get_random_secret_key())`
    
Копируем строку в `.env` файл: `DJANGO_KEY='ваш ключ'` 

Так же в проекте используются следующие переменные окружения:  
`DEBUG`.  Вкючение/выключение режима отладки. Значение False - выключение режима отладки. Значение True - включение режима отладки.  
`ALLOWED_HOSTS`. Список строк, представляющих имена хостов/доменов, которые может обслуживать ваш Django-сайт.  

### 5. Переходим в директорию проекта и выполняем миграции в БД: 
```
python manage.py migrate
```

## Использование:

### 1. Создаем панель администратора:

```
python manage.py createsuperuser
```


### 2. Запускаем сервер:

```
python manage.py runserver
```


### 3. Переходим на http://127.0.0.1:8000/ и видим наш сайт.

## Источники данных

1. Фронтенд получает данные из базы данных SQLite3. Данные вы можете вносить через панель администратора.
2. Так же вы можете вносить данные используя файлы формата .json через скрипт `load_place.py` расположенный в папке ../poster/managment/commands/    
По умолчанию скрипт ищет файлы используя путь `./static/places/`. Для этого создайте папку `places` в папке `static` и положите туда файл .json с данными как указано ниже и после этого запустите скрипт в терминале.    
```
python manage.py load_place
```
Или, если вы хотите хранить .json файлы в другом месте, укажите путь к ним в аргументе к скрипту:
```
python manage.py load_place --path <путь до файла>
```
    
```
{
    "title": "Экскурсионная компания «Легенды Москвы»",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/4f793576c79c1cbe68b73800ae06f06f.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/7a7631bab8af3e340993a6fb1ded3e73.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/a55cbc706d764c1764dfccf832d50541.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/65153b5c595345713f812d1329457b54.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/0a79676b3d5e3b394717b4bf2e610a57.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/1e27f507cb72e76b604adbe5e7b5f315.jpg"
    ],
    "description_short": "Неважно, живёте ли вы в Москве всю жизнь или впервые оказались в столице, составить ёмкий, познавательный и впечатляющий маршрут по городу — творческая и непростая задача. И её с удовольствием берёт на себя экскурсионная компания «Легенды Москвы»!",
    "description_long": "<p>Экскурсия от компании «Легенды Москвы» — простой, удобный и приятный способ познакомиться с городом или освежить свои чувства к нему. Что выберете вы — классическую или необычную экскурсию, пешую прогулку или путешествие по городу на автобусе? Любые варианты можно скомбинировать в уникальный маршрут и создать собственную индивидуальную экскурсионную программу.</p><p>Компания «Легенды Москвы» сотрудничает с аккредитованными экскурсоводами и тщательно следит за качеством экскурсий и сервиса. Автобусные экскурсии проводятся на комфортабельном современном транспорте. Для вашего удобства вы можете заранее забронировать конкретное место в автобусе — это делает посадку организованной и понятной.</p><p>По любым вопросам вы можете круглосуточно обратиться по телефонам горячей линии.</p><p>Подробности узнавайте <a class=\"external-link\" href=\"https://moscowlegends.ru \" target=\"_blank\">на сайте</a>. За обновлениями удобно следить <a class=\"external-link\" href=\"https://vk.com/legends_of_moscow \" target=\"_blank\">«ВКонтакте»</a>, <a class=\"external-link\" href=\"https://www.facebook.com/legendsofmoscow?ref=bookmarks \" target=\"_blank\">в Facebook</a>.</p>",
    "coordinates": {
        "lng": "37.64912239999976",
        "lat": "55.77754550000014"
    }
}
```


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org/).

 
