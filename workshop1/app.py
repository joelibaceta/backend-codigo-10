from flask import Flask
from flask import render_template
from flask import send_file
from flask import request

from flaskext.mysql import MySQL

mysql = MySQL(host="localhost", user="root", 
              password="rootcodigo", db="movies")

app = Flask(__name__)
mysql.init_app(app)
conn = mysql.connect()

def prepare_data(movies):

    final_movies = []

    q = "SELECT mg.idMovie, g.Title FROM moviegenre AS mg "
    q = q + "LEFT JOIN genre AS g ON mg.idGenre = g.idGenre "
    q = q + "WHERE idMovie = "

    for movie in movies:
        cursor = conn.cursor()
        query = q + str(movie[0])
        cursor.execute(query)
        results = cursor.fetchall()
        genres = list(map(lambda x: x[1], results))
        modified_movie = list(movie)
        modified_movie.append(", ".join(genres))
        final_movies.append(modified_movie)

    return final_movies

def show_movies(filters=None):
    cursor = conn.cursor()
    query = "SELECT * FROM movie "
    if filters != None:
        query = query + filters
    cursor.execute(query)
    results = cursor.fetchall()
    data = prepare_data(results)
    return render_template("index.html", movies = data)


@app.route("/")
def hello_world():
    return("hello world")

# /movies/from/2016/to/2018
@app.route("/movies/from/<begin>/to/<to>")
def movies_by_range(begin, to):
    filter = f"WHERE year BETWEEN {begin} AND {to}"
    return show_movies(filter)

@app.route("/movies")
def list_movies():
    filter = None
    q = request.args.get('q')
    if q != None:
        filter = filter + f"WHERE Title LIKE '%{q}%' "
        filter = filter + f"OR Director LIKE '%{q}%' "
        filter = filter + f"OR Plot LIKE '%{q}%' "
    return show_movies(filter)

@app.route("/styles.css")
def styles():
    return send_file("./assets/styles.css")
