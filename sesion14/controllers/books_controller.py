from flask_restful import Resource

from sesion14.models.book import Book
from sesion14.schemas.book import BookSchema

class BooksController(Resource):
    
    def get(self):
        books = Book.query.all()
        schema = BookSchema()
        data = schema.dump(books, many=True)
        return data