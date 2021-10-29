from flask_restful import Resource

from sesion14.models.category import Category
from sesion14.schemas.category import CategorySchema

class CategoriesController(Resource):
    
    def get(self):
        categories = Category.query.all()
        schema = CategorySchema()
        data = schema.dump(categories, many=True)
        return data