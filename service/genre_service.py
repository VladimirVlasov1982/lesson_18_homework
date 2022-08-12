from dao.genres_dao import GenreDAO


class GenreService:
    """Сервисы жанра"""

    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self):
        # Получить все жанры
        return self.dao.get_all()

    def get_by_id(self, gid: int):
        # Получить жанр по его id
        return self.dao.get_by_id(gid)
