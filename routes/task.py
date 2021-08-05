from controllers import taskController
from flask import request
from config import firebase
import os

storage = firebase.storage()

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
            'state': '',
            'description': '',
            'turn': ''
        }

        if request.method == 'POST':
            try:
                for data in dataForm:
                    dataForm[data] = request.form[data]

                return taskController.setPendingTask(dataForm)
            except:
                return {'message': 'Faltan completar algunos campos.'}

    @app.route(url+'set-finished-task', methods=['GET', 'POST'])
    def setFinishedTask():
        dataForm = {
            'type': '',
            'turn': '',
            'startTime': '',
            'endTime': '',
            'hourMan': '',
            'description': '',
        }

        images = {}
        if request.method == 'POST':
            imageBefore = request.files['image-before']
            imageAfter = request.files['image-after']
            mainRouteForImage = app.config['UPLOAD_FOLDER']

            images['image-before'] = imageBefore.save(os.path.join(mainRouteForImage, 'before'))
            images['image-after'] =  imageAfter.save(os.path.join(mainRouteForImage, 'after'))
            images['url-local-images'] = app.config['UPLOAD_FOLDER']

            for data in dataForm:
                dataForm[data] = request.form[data]

            try:
                return taskController.setFinishedTask(dataForm, images)
            except:
                return 'Error al agregar tarea finalizada'

    @app.route(url+'get-hours', methods=['GET'])
    def getHours():
        return taskController.getHours()
        
    @app.route(url+'get-hour', methods=['GET'])
    def getHour():
        typeTask = request.args.get('task-type')
        return taskController.getHoursBy(typeTask)