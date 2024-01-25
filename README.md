## Название проекта
Укажите название вашего проекта.

Currency Converter

## Описание проекта

Небольшой django проект для отображения актуального курса доллара к рублю с помощью сервиса Fixer.io. Сервис отображает последние 10 запросов к внешнему API.
Нужно добавить свой ключ в файл .env в строке API_KEY.

Доступны 2 функции - получить текущий курс доллара к рублю и удалить все сохранненые ранее запросы.

## Технологии

Django, python-dotenv, requests

## Как запустить проект

1. Создание виртуального окружения

` python -m venv venv `

Для активации виртуального окружения нажмите: 

` venv/Scripts/activate `

2. Установавка всех необходимых компонентов из файла requirements.txt.

` pip install -r requirements.txt `

3. Запуск проекта на локальном сервере

`cd currency_exchange`
` python manage migrate ` - запуск миграций
` python manage makemigrations `
` python manage runserver ` - запуск сервера

`http://127.0.0.1:8000/exchange_app/get-current-usd/ ` - ссылка для отображения текущего курса валют 

Будет отображаться 10 последних запросов по курсу валют, для появления текущего курса необходимо обновить страницу.

`http://127.0.0.1:8000/exchange_app/delete-rates/ ` - ссылка для удаления всех сохраненных ранее курсов валют 
