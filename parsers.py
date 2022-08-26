from flask_restx.reqparse import RequestParser

movie_parser: RequestParser = RequestParser()
movie_parser.add_argument(name="id", type=int)
movie_parser.add_argument(name="title", type=str, required=False)
movie_parser.add_argument(name="description", type=str, required=False)
movie_parser.add_argument(name="trailer", type=str, required=False)
movie_parser.add_argument(name="year", type=int, required=False)
movie_parser.add_argument(name="rating", type=float, required=False)
movie_parser.add_argument(name="genre_id", type=int, required=False)
movie_parser.add_argument(name="director_id", type=int, required=False)


