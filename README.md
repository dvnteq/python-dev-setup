Book Library API

API для управления библиотекой книг на FastAPI + PostgreSQL

Описание

Проект предоставляет REST API для работы с библиотекой книг. Позволяет управлять категориями и книгами: создавать, читать, обновлять и удалять записи.

Технологии

- Python 3
- FastAPI
- SQLAlchemy
- PostgreSQL
- Uvicorn
- Pydantic

Установка и запуск

1. Клонирование репозитория
bash
git clone <URL_вашего_репозитория>
cd <имя_папки_проекта>

2. Создание и активация виртуального окружения
bash
python3 -m venv venv
source venv/bin/activate

3. Установка зависимостей
bash
pip install -r requirements.txt

4. Запуск PostgreSQL

bash
sudo service postgresql start

5. Настройка переменных окружения

Создайте файл .env в корне проекта и добавьте:
DB_HOST=localhost
DB_PORT=5432
DB_NAME=octagon_db
DB_USER=octagon
DB_PASSWORD=12345

6. Инициализация базы данных

bash
python -m app.init_db

7. Запуск API

bash
uvicorn app.main:app --reload

Использование

После запуска сервер будет доступен по адресу: **http://127.0.0.1:8000**

Основные эндпоинты

 Health Check
- GET /health - проверка работоспособности API

 Категории
- GET /categories/ - получить все категории
- GET /categories/{id} - получить категорию по ID
- POST /categories/ - создать категорию
- PUT /categories/{id} - обновить категорию
- DELETE /categories/{id} - удалить категорию

 Книги
- GET /books/ - получить все книги
- GET /books/?category_id={id} - получить книги по категории
- GET /books/{id} - получить книгу по ID
- POST /books/ - создать книгу
- PUT /books/{id} - обновить книгу
- DELETE /books/{id} - удалить книгу