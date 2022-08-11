from dao.model.models import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Genre).all()

    def get_by_id(self, gid: int):
        return self.session.query(Genre).get(gid)