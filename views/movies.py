from flask import request
from flask_restx import Resource, Namespace
from implemented import movie_service
from dao.model.shemas import MovieSchema

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        """Возвращает все фильмы, фильмы по режиссеру, жанру и году"""
        req = request.args
        if req:
            return movies_schema.dump(movie_service.get_by_request(req)), 200
        return movies_schema.dump(movie_service.get_all()), 200

    def post(self):
        """Добавляет фильм"""
        return movie_schema.dump(movie_service.create(request.json)), 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):

    def get(self, mid: int):
        """Возвращает фильм по его id"""
        return movie_schema.dump(movie_service.get_by_id(mid)), 200

    def put(self, mid: int):
        """Изменение фильма"""
        req_json = request.json
        req_json['id'] = mid
        return movie_schema.dump(movie_service.update(req_json)), 204

    def delete(self, mid: int):
        """Удаляет фильм"""
        movie_service.delete(mid)
        return "", 204
