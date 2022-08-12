from dao.movies_dao import MovieDAO


class MovieService:
    """Сервисы фильма"""

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        # Получить все фильмы
        return self.dao.get_all()

    def get_by_id(self, mid: int):
        # Получить фильм по его id
        return self.dao.get_by_id(mid)

    def get_by_request(self, data):
        # Получить фильмы по id режиссера, id жанра и году
        if "director_id" in data:
            movies = self.dao.get_by_director(data.get('director_id'))
            return movies
        if "genre_id" in data:
            movies = self.dao.get_by_genre(data.get('genre_id'))
            return movies
        if "year" in data:
            movies = self.dao.get_by_year(data.get('year'))
            return movies
        return None

    def create(self, data):
        # Добавление нового фильма
        return self.dao.create(data)

    def update(self, data):
        # Обновление фильма
        try:
            mid = data.get('id')
            movie = self.dao.get_by_id(mid)
            movie.title = data.get('title')
            movie.description = data.get('description')
            movie.trailer = data.get('trailer')
            movie.year = data.get('year')
            movie.rating = data.get('rating')
            movie.genre_id = data.get('genre_id')
            movie.director_id = data.get('director_id')
            return self.dao.update(movie)
        except Exception:
            return None

    def delete(self, mid: int):
        # Удаление фильма
        movie = self.dao.get_by_id(mid)
        return self.dao.delete(movie)
