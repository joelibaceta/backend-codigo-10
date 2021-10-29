from flask_restful import Resource

from sesion14.models.category import Category
from sesion14.schemas.book import BookSchema

class BooksByCategoryController(Resource):

    def get(self, id):
        category = Category.query.get(id)
        books = category.books
        schema = BookSchema()
        data = schema.dump(books, many=True)
        return data