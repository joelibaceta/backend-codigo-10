from web3.models.task import Task

from flask import redirect

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
        pass

    def delete(id):
        pass