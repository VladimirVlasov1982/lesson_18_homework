# Здесь схемы сериализации
from marshmallow import Schema, fields


class MovieSchema(Schema):
    """Схема фильма"""
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Integer()
    rating = fields.Float()
    genre = fields.Nested('GenreSchema')
    director = fields.Nested('DirectorSchema')


class DirectorSchema(Schema):
    """Схема режиссера"""
    id = fields.Int()
    name = fields.Str()


class GenreSchema(Schema):
    """Схема жанра"""
    id = fields.Int()
    name = fields.Str()
