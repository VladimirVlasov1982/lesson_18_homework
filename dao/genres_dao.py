from dao.model.models import Genre


class GenreDAO:
    """DAO жанры"""

    def __init__(self, session):
        self.session = session

    def get_all(self):
        # Получить все жанры
        return self.session.query(Genre).all()

    def get_by_id(self, gid: int):
        # Получить жанр по его id
        return self.session.query(Genre).get(gid)
