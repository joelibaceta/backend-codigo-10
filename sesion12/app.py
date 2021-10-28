from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask import render_template

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://developer:password@localhost/movies"
db = SQLAlchemy(app)



@app.route("/")
def hello_world():
    return "hello world"

@app.route("/movies")
def get_movies():
    results = db.session.execute("SELECT * FROM carterlera")
    return render_template("index.html", rows = results)