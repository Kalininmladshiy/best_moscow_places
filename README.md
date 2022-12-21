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
По умолчанию скрипт ищет файлы используя путь `./static/places/`. Для этого создайте папку `places` в папке `static` и положите туда файл .json с данными как указано на скриншоте ниже и после этого запустите скрипт в терминале.    
```
python manage.py load_place
```
Или, если вы хотите хранить .json файлы в другом месте, укажите путь к ним в аргументе к скрипту:
```
python manage.py load_place --path <путь до файла>
```
    

![изображение](https://user-images.githubusercontent.com/106922768/206469607-fcf11afc-6f9c-4501-b6be-937c8427fff1.png)


## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org/).

 
