from dao.model.models import Director


class DirectorDAO:
    """DAO режиссеры"""

    def __init__(self, session):
        self.session = session

    def get_all(self):
        # Получить всех режиссеров
        return self.session.query(Director).all()

    def get_by_id(self, did: int):
        # Получить режиссера по его id
        return self.session.query(Director).get(did)
