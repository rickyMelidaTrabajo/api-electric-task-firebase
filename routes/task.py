from controllers import taskController
from flask import request


def task(app, url):

    @app.route(url+'get-tasks', methods=['GET'])
    def getTasks():
        return taskController.getTasks()

    @app.route(url+'get-pending-task', methods=['GET'])
    def getPendingTask():
        return taskController.getPendingTasks()

    @app.route(url+'get-finished-task', methods=['GET'])
    def getFinishedTask():
        return taskController.getFinishedTasks()

    @app.route(url+'set-pending-task', methods=['GET', 'POST'])
    def setPendingTask():
        if request.method == 'POST':
            type = request.form['type']
            state = request.form['state']
            description = request.form['description']
            turn = request.form['turn']

            data = {
                'type': type,
                'state': state,
                'description': description,
                'turn': turn
            }

        return taskController.setPendingTask(data)

    @app.route(url+'set-finished-task', methods=['GET', 'POST'])
    def setFinishedTask():
        return 'This is setFinishedTask route'
