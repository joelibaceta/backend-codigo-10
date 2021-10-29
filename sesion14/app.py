from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_marshmallow import Marshmallow

app = Flask(__name__)

conn_string = "mysql+pymysql://dev:123456@localhost/library"
app.config['SQLALCHEMY_DATABASE_URI'] = conn_string

db = SQLAlchemy(app)
api = Api(app)
ma = Marshmallow(app)

@app.route("/")
def hello_world():
    return "hello world"

from sesion14.controllers.books_controller import BooksController
from sesion14.controllers.book_controller import BookController
from sesion14.controllers.categories_controller import CategoriesController
from sesion14.controllers.category_controller import CategoryController
from sesion14.controllers.authors_controller import AuthorsController
from sesion14.controllers.author_controller import AuthorController


api.add_resource(BooksController, "/books")
api.add_resource(BookController, "/book/<id>")
api.add_resource(CategoriesController, "/categories")
api.add_resource(CategoryController, "/category/<id>")
api.add_resource(AuthorsController, "/authors")
api.add_resource(AuthorController, "/author/<id>")

# /category/<id>/books