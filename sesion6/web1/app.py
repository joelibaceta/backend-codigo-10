from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello World</h1>"


# Query Params
# =============
#
# localhost:5000/hello?name=joel

@app.route("/hello")
def hello_name():
    name = request.args.get('name')
    if name == None:
        name = "Anonimo"
    return f"<h1>Hello {name}</h1>"

# URL Params
# ==========
#
# localhost:5000/hello/Juan

@app.route("/hello/<name>")
def hello_name_2(name):
    return f"<h1>Hello {name}</h1>"
