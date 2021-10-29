from flask_restful import Resource

from sesion14.models.author import Author
from sesion14.schemas.author import AuthorSchema

class AuthorController(Resource):
    
    def get(self, id):
        author = Author.query.get(id)
        schema = AuthorSchema()
        data = schema.dump(author)
        return data