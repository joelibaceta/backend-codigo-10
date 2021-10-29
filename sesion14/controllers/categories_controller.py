from flask_restful import Resource
from flask import request

from sesion14.models.category import Category
from sesion14.schemas.category import CategorySchema

from sesion14.app import db

class CategoriesController(Resource):
    
    def get(self):
        categories = Category.query.all()
        schema = CategorySchema()
        data = schema.dump(categories, many=True)
        return data

    def post(self):
        data = request.json
        new_category = Category(**data)
        db.session.add(new_category)
        db.session.commit()
        return {"status": "ok"}, 201