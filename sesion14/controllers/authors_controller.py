from flask_restful import Resource
from flask import request 

from sesion14.models.author import Author
from sesion14.schemas.author import AuthorSchema

from sesion14.app import db

class AuthorsController(Resource):
    
    def get(self):
        authors = Author.query.all()
        schema = AuthorSchema()
        data = schema.dump(authors, many=True)
        return data
    
    def post(self):
        data = request.json
        new_author = Author(**data)
        db.session.add(new_author)
        db.session.commit()
        return {"status": "ok"}, 201