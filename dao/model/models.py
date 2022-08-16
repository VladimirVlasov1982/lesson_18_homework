# здесь модель SQLAlchemy для сущности
from setup_db import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


class Movie(BaseModel):
    """Модель фильма"""
    __tablename__ = "movie"
    title = db.Column(db.String(250))
    description = db.Column(db.Text)
    trailer = db.Column(db.String)
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    genre = db.relationship('Genre')
    director = db.relationship('Director')


class Director(BaseModel):
    """Модель режиссера"""
    __tablename__ = "director"
    name = db.Column(db.String(100))


class Genre(BaseModel):
    """Модель жанра"""
    __tablename__ = "genre"
    name = db.Column(db.String(100))
