from flask_restful import Resource

from sesion14.models.category import Category
from sesion14.schemas.category import CategorySchema

class CategoryController(Resource):
    
    def get(self, id):
        category = Category.query.get(id)
        schema = CategorySchema()
        data = schema.dump(category)
        return data