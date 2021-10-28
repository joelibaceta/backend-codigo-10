from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask_restful import  Api


app = Flask(__name__)

api = Api(app)
ma =  Marshmallow(app)

connection_string = "mysql+pymysql://developer:password@localhost/movies"
app.config['SQLALCHEMY_DATABASE_URI'] = connection_string

db = SQLAlchemy(app)

from sesion13.controllers.movie_controller import MovieController


@app.route("/")
def hello_world():
    return "hello world"

api.add_resource(MovieController, "/movies")