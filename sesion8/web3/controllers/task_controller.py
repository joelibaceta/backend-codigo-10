from web3.models.task import Task

from flask import redirect

import json

class TaskController:

    tasks = []

    def list():
        pass

    def get(id):
        pass

    def create(req):
        print("Creando tarea")
        form_data = req.form
        task_name = form_data['taskname']

        id = len(TaskController.tasks)
        new_task = Task(id, task_name)

        TaskController.tasks.append(new_task)
        return redirect('/')


    def update(id, req):

        body = json.loads(req.data.decode())

        index = 0
        for idx, task in enumerate(TaskController.tasks):
            if int(task.id) == int(id):
                index = idx

        if "title" in body: 
            title = body["title"]
            TaskController.tasks[index].title = title

        if "status" in body: 
            status = body["status"]
            TaskController.tasks[index].status = status

        return "OK"

    def delete(id):
        for task in TaskController.tasks:
            if int(task.id) == int(id):
                print(f"Elimino: {task}")
                TaskController.tasks.remove(task)
        return redirect('/')
