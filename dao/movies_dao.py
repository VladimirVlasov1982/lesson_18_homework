from dao.model.models import Movie
from constants import PER_PAGE

class MovieDAO:
    """DAO фильмы"""

    def __init__(self, session):
        self.session = session

    def get_all(self):
        # Получить все фильмы
        return self.session.query(Movie).all()

    def get_by_id(self, mid: int):
        # Получить фильм по его id
        return self.session.query(Movie).get(mid)

    def get_by_director(self, director_id):
        # Получить фильмы по id режиссера
        movies = self.session.query(Movie).filter(Movie.director_id == director_id).all()
        return movies

    def get_by_genre(self, genre_id):
        # Получить фильмы по id жанра
        movies = self.session.query(Movie).filter(Movie.genre_id == genre_id).all()
        return movies

    def get_by_year(self, year):
        # Получить фильмы по году
        movies = self.session.query(Movie).filter(Movie.year == year).all()
        return movies

    def create(self, data):
        # Добавление нового фильма
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie):
        # Обновление фильма
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, movie):
        # Удаление фильма
        self.session.delete(movie)
        self.session.commit()
