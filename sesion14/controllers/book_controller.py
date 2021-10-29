from flask_restful import Resource

from sesion14.models.book import Book
from sesion14.schemas.book import BookSchema

class BookController(Resource):
    
    def get(self, id):
        book = Book.query.get(id)
        schema = BookSchema()
        data = schema.dump(book)
        return data