from flask import Flask
from flask import render_template
from flask import send_file

from flaskext.mysql import MySQL

mysql = MySQL(host="localhost", user="root", 
              password="rootcodigo", db="movies")

app = Flask(__name__)
mysql.init_app(app)
conn = mysql.connect()

@app.route("/")
def hello_world():
    return("hello world")

@app.route("/movies")
def list_movies():
    cursor = conn.cursor()
    query = "SELECT * FROM movie"
    cursor.execute(query)
    results = cursor.fetchall()
    print(results)
    return render_template("index.html", movies = results)

@app.route("/styles.css")
def styles():
    return send_file("./assets/styles.css")
