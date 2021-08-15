from controllers import taskController
from flask import request
from config import firebase
import os
import json

storage = firebase.storage()

def task(app, url):

    @app.route(url+'get-tasks', methods=['GET'])
    def getTasks():
        return taskController.getTasks()

    @app.route(url+'get-pending-tasks', methods=['GET'])
    def getPendingTask():
        return taskController.getPendingTasks()

    @app.route(url+'get-finished-tasks', methods=['GET'])
    def getFinishedTask():
        return taskController.getFinishedTasks()

    @app.route(url+'set-pending-task', methods=['GET', 'POST'])
    def setPendingTask():
        dataForm = {
            'type': '',
            'description': '',
            'turn': '',
            'username': ''
        }

        if request.method == 'POST':
            request_data = request.get_json()
            try:
                try:
                    for data in dataForm:
                        dataForm[data] = request.form[data]
                except:
                    for data in dataForm:
                        dataForm[data] = request_data[data]

                return taskController.setPendingTask(dataForm)
            except:
                return {'message': 'Faltan completar algunos campos.'}

    @app.route(url+'set-finished-task', methods=['GET', 'POST'])
    def setFinishedTask():
        dataForm = {
            'type': '',
            'turn': '',
            'start_time': '',
            'end_time': '',
            'hour_man': '',
            'description': '',
            'username': ''
        }

        images = {}

        if request.method == 'POST':

            try:
                imageBefore = request.files['image_before']
                imageAfter = request.files['image_after']
                mainRouteForImage = app.config['UPLOAD_FOLDER']

                images['image_before'] = imageBefore.save(os.path.join(mainRouteForImage, 'before'))
                images['image_after'] =  imageAfter.save(os.path.join(mainRouteForImage, 'after'))
                images['url-local-images'] = app.config['UPLOAD_FOLDER']

                try:
                    taskData = json.loads(request.form['data'])

                    for data in dataForm:
                        dataForm[data] = taskData[data]
                except:
                    request_data = request.get_json()

                    for data in dataForm:
                        dataForm[data] = request_data[data]

                return taskController.setFinishedTask(dataForm, images)
            except:
                return {'message': 'Faltan completar algunos campos desde el backend.'}


    @app.route(url+'get-hours', methods=['GET'])
    def getHours():
        return taskController.getHours()

    @app.route(url+'get-hour', methods=['GET'])
    def getHour():
        typeTask = request.args.get('task-type')
        return taskController.getHoursBy(typeTask)
