# api_final
api final
# API для Yatube

## Описание
REST API для социальной сети Yatube.

## Установка
1. Клонировать репозиторий
2. Установить зависимости: pip install -r requirements.txt
3. Выполнить миграции: python manage.py migrate
4. Создать суперпользователя: python manage.py createsuperuser
5. Запустить сервер: python manage.py runserver

## Примеры запросов

### Получение токена
POST /api/v1/jwt/create/
{
    "username": "user",
    "password": "pass"
}

### Подписка на пользователя
POST /api/v1/follow/
Authorization: Bearer <token>
{
    "following": "username"
}

## Документация
http://127.0.0.1:8000/redoc/