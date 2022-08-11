from dao.model.models import Director


class DirectorDAO:

    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Director).all()

    def get_by_id(self, did: int):
        return self.session.query(Director).get(did)
