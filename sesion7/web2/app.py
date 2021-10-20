from flask import Flask
from flask import request
from flask import render_template
from flask import send_file
from flask import send_from_directory

from PIL import Image

app = Flask(__name__)

print(__name__)

tasks = []

@app.route("/")
def hello_world():
    msg = "<h1>Hello World</h1> "
    msg = msg + "<ul>"
    for task in tasks:
        msg = msg + f"<li>{task}</li>"
    msg = msg + "</ul>"
    return msg

@app.route("/home")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/contact")
def contact():
    return render_template("contactanos.html", tasks=tasks)


@app.route("/tasks", methods=['POST'])
def new_task():
    content = request.json
    tasks.append(content["title"])
    return "Agregado"

@app.route('/rotate/<picture>/<degrees>')
def rotatepic(picture, degrees):
    im = Image.open('./assets/' + picture)
    angle = int(degrees)
    output = im.rotate(angle)
    output.save('output.jpg')
    return send_file('output.jpg')

@app.route('/humans.txt')
def humans():
    return send_file('./assets/humans.txt')

@app.route('/main.css')
def styles():
    return send_file('./assets/style.css')

@app.route('/assets/<path:filename>')
def find_in_folder(filename):
    return send_from_directory("./assets", filename)