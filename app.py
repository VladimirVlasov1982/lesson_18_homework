# Основной файл приложения. здесь конфигурируется фласк, сервисы, SQLAlchemy
import logging
from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.movies import movie_ns
from views.directors import director_ns
from views.genres import genre_ns


def create_app(config_object):
    # Функция создания основного объекта app
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.url_map.strict_slashes = False
    app.app_context().push()
    register_extensions(app)
    return app


def register_extensions(app):
    # Функция подключения расширений и создание базы данных
    db.init_app(app)
    api = Api(app)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)


app = create_app(Config)

if __name__ == '__main__':
    app.run(host="localhost", port=10001)
