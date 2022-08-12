# здесь модель SQLAlchemy для сущности
from setup_db import db


class Movie(db.Model):
    """Модель фильма"""
    __tablename__ = "movie"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    description = db.Column(db.Text)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    genre = db.relationship('Genre')
    director = db.relationship('Director')


class Director(db.Model):
    """Модель режиссера"""
    __tablename__ = "director"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


class Genre(db.Model):
    """Модель жанра"""
    __tablename__ = "genre"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
