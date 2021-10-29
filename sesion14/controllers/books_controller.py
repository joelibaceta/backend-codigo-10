from flask_restful import Resource
from flask import request

from sesion14.models.author import Author
from sesion14.models.book import Book
from sesion14.schemas.book import BookSchema

from sesion14.app import db

from sqlalchemy import and_

class BooksController(Resource):
    
    def get(self):
        books = Book.query.all()
        schema = BookSchema()
        data = schema.dump(books, many=True)
        return data

    def post(self):
        data = request.json

        authors_names = data["authors"]
        data.pop("authors")

        new_book = Book(**data)

        new_book.authors = []   

        if authors_names != None:
            for author_name in authors_names:
                (fname, lname) = author_name.split(" ")

                new_author = Author(first_name= fname, last_name=lname)
                new_book.authors.append(new_author)

        db.session.add(new_book)
        db.session.commit()
        return {"status": "ok"}, 201