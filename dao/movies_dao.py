from dao.model.models import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_id(self, mid: int):
        return self.session.query(Movie).get(mid)

    def get_by_director(self, director_id):
        movies = self.session.query(Movie).filter(Movie.director_id == director_id).all()
        return movies

    def get_by_genre(self, genre_id):
        movies = self.session.query(Movie).filter(Movie.genre_id == genre_id).all()
        return movies

    def get_by_year(self, year):
        movies = self.session.query(Movie).filter(Movie.year == year).all()
        return movies

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, movie):
        self.session.delete(movie)
        self.session.commit()