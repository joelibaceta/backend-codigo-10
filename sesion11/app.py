from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template
from flask import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:rootcodigo@localhost/movies"
db = SQLAlchemy(app)

from sesion11.models.movie import Movie

@app.route("/")
def helloworld():
    return "hello world"

@app.route("/movies")
def list_movies():
    movies = Movie.query.filter().order_by("Year") 
    return render_template("index.html", movies = movies)

@app.route("/movies", methods = ["POST", ])
def new_movie():
    data = request.json
    Movie.create_movie(**data)
    return "OK"

@app.route("/movie/<id>", methods = ["PUT", "DELETE"])
def update_movie(id):
    movie = Movie.query.filter_by(id=id)
    if request.method == "PUT":
        data = request.json
        movie.update(data)
        db.session.commit()
    else:
        db.session.delete(movie.first())
        db.session.commit()
    return "OK"

