from dao.directors_dao import DirectorDAO


class DirectorService:
    """Сервис режиссера"""

    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self):
        # Получить всех режиссеров
        return self.dao.get_all()

    def get_by_id(self, did: int):
        # Получить режиссера по его id
        return self.dao.get_by_id(did)
