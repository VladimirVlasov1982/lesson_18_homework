# Создание DAO и сервисов чтобы импортировать их везде
from dao.base_dao import BaseDAO
from dao.model.models import Genre, Director, Movie
from dao.movies_dao import MovieDAO
from service.base_service import BaseService


from service.movie_service import MovieService
from setup_db import db

movie_dao = MovieDAO(db.session, Movie)
movie_service = MovieService(movie_dao)

director_dao = BaseDAO(db.session, Director)
director_service = BaseService(director_dao)

genre_dao = BaseDAO(db.session, Genre)
genre_service = BaseService(genre_dao)
