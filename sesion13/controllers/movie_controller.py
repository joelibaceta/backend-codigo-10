
from flask_restful import Resource

from sesion13.models.movie import Movie
from sesion13.schemas.movie_schema import MovieSchema

class MovieController(Resource):

    def get(self):
        movies = Movie.query.all()
        #results = map(lambda x: x.title, movies)
        #return ", ".join(results)
        schema = MovieSchema()
        data = schema.dump(movies, many=True)
        return data