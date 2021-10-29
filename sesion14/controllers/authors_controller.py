from flask_restful import Resource

from sesion14.models.author import Author
from sesion14.schemas.author import AuthorSchema

class AuthorsController(Resource):
    
    def get(self):
        authors = Author.query.all()
        schema = AuthorSchema()
        data = schema.dump(authors, many=True)
        return data