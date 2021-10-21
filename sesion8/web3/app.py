from flask import Flask
from flask import render_template
from flask import request

from flask_bootstrap import Bootstrap

from web3.controllers.task_controller import TaskController

app = Flask(__name__)

Bootstrap(app)

@app.route('/')
def hello_world():
    tasks = TaskController.tasks
    return render_template("index.html", tasks=tasks)

@app.route('/deletetask/<id>')
def delete_task(id):
    return TaskController.delete(id)

@app.route('/tasks', methods = ['POST', 'GET'])
def list_or_create():
    if request.method == 'GET':
        return TaskController.list()
    else:
        return TaskController.create(request)

@app.route('/task/<id>', methods = ['PUT', 'GET', 'DELETE'])
def get_update_or_delete(id):
    if request.method == 'PUT':
        return TaskController.update(id, request)
    elif request.method == 'GET':
        return TaskController.get(id)
    else:
        return TaskController.delete(id)

