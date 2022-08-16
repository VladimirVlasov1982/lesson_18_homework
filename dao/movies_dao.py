from dao.base_dao import BaseDAO


class MovieDAO(BaseDAO):
    """DAO фильмы"""

    def get_by_director(self, director_id):
        # Получить фильмы по id режиссера
        movies = self.session.query(self.model).filter(self.model.director_id == director_id).all()
        return movies

    def get_by_genre(self, genre_id):
        # Получить фильмы по id жанра
        movies = self.session.query(self.model).filter(self.model.genre_id == genre_id).all()
        return movies

    def get_by_year(self, year):
        # Получить фильмы по году
        movies = self.session.query(self.model).filter(self.model.year == year).all()
        return movies

    def create(self, data):
        # Добавление нового фильма
        movie = self.model(**data)
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
