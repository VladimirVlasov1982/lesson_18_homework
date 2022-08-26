from flask_sqlalchemy import Model

from dao.base_dao import BaseDAO


class BaseService:
    """Базовый сервис"""

    def __init__(self, dao: BaseDAO):
        self.dao = dao

    def get_all(self) -> list[Model]:
        # Получить все
        return self.dao.get_all()

    def get_by_id(self, gid: int) -> Model | None:
        # Получить по id
        return self.dao.get_by_id(gid)
