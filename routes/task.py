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
        dataForm = {
            'type': '',
            'description': '',
            'turn': ''
        }

        #_id
        #taskNumber
        #type = request.form['type']
        #state = 'Pendiente'
        #description = request.form['description']
        #dateGeneration
        #turn = request.form['turn']
        #name
        #position
        if request.method == 'POST':

            for data in dataForm:
                dataForm[data] = request.form[data]

        return taskController.setPendingTask(dataForm)

    @app.route(url+'set-finished-task', methods=['GET', 'POST'])
    def setFinishedTask():
        dataForm = {
            'type': '',
            'turn': '',
            'startTime': '',
            'endTime': '',
            'hourMan': '',
            'description': '',
            #'imageBefore': '',
            #'imageAfter': ''
        }
        if request.method == 'POST':
            #_id
            #taskNumber
            #type = request.form['type']
            #state = 'Finalizado'
            #description = request.form['description']
            #dateGeneration
            #dateClosing
            #startTime = request.form['start-time']
            #endTime = request.form['end-time']
            #hourMan = request.form['hour-man']
            #imageBefore
            #imageAfter
            #turn = request.form['turn']
            #name
            #position

            for data in dataForm:
                dataForm[data] = request.form[data]

            try:
                return taskController.setFinishedTask(dataForm)
            except:
                return 'Error al agregar tarea finalizada'
