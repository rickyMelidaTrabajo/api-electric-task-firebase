from config import firebase
import uuid
import controllers.numberTasks as TaskNumber
import controllers.technicianController as Technician
from datetime import datetime, timedelta
from flask.globals import request
from flask import session
import os

db = firebase.database()
storage = firebase.storage()

def getPendingTasks():
    tasks = []
    try:
        pendingTasks = db.child('tasks').child('pending-tasks').get()
        for task in pendingTasks.each():
            tasks.append(task.val())
        return {'tasks': tasks}
    except:
        return 'No hay tareas pendientes'


def getFinishedTasks():
    try:
        tasks = []
        finishedTasks = db.child('tasks').child('finished-tasks').get()
        for task in finishedTasks.each():
            tasks.append(task.val())
        return {'tasks': tasks, 'lenght': len(tasks)}
    except:
        return 'No ha tareas finalizadas'


def setPendingTask(dataForm):
    technician = Technician.getWithUsername(dataForm['username'])['techs']

    dataForm['_id'] = uuid.uuid1().hex
    dataForm['task_number'] = TaskNumber.getNumberTasks(db) + 1
    dataForm['date_generation'] = datetime.now().strftime('%d-%m-%Y')
    dataForm['name'] = technician[0]['name']
    dataForm['position'] = technician[0]['position']
    dataForm['state'] = 'Pendiente'

    try:
        db.child('tasks').child('pending-tasks').push(dataForm)
        return {'message': 'Se ha agregado correctamente la tarea', 'taskNumber': dataForm['task_number']}
    except:
        return 'No se pudo agregar la tarea'


def setFinishedTask(dataForm, images):

    tasks = setAllTasks(dataForm, images)

    try:
        db.child('tasks').child('finished-tasks').push(tasks)
        return {'message': 'Se ha agregado correctamente la tarea'}
    except:
        return {'message': 'No se pudo agregar la tarea'}


def setAllTasks(dataForm, images):
    dataFinishedTask = dataForm

    try:
        technician = Technician.getWithUsername(dataForm['username'])['techs']

        dataFinishedTask['_id'] = uuid.uuid1().hex
        dataFinishedTask['task_number'] = int(TaskNumber.getNumberTasks(db)) + 1
        dataFinishedTask['state'] = 'Finalizado'
        dataFinishedTask['date_generation'] = datetime.now().strftime('%d-%m-%Y')
        dataFinishedTask['date_closing'] = datetime.now().strftime('%d-%m-%Y')
        dataFinishedTask['name'] = technician[0]['name']
        dataFinishedTask['position'] = technician[0]['position']

        imagesStorage = saveImageStorage(images, dataForm['task_number'])

        dataFinishedTask['image_before'] = imagesStorage['before']
        dataFinishedTask['image_after'] = imagesStorage['after']

        return dataFinishedTask
    except:
        return 'Error al setear todas las tareas'


def saveImageStorage(images, numTask):
    routeStorage = 'tasks/' + str(numTask) + '/'

    try:
        storage.child(routeStorage + 'before').put(os.path.join(images['url-local-images'], 'before'))
        storage.child(routeStorage + 'after').put(os.path.join(images['url-local-images'], 'after'))

        urlBefore = storage.child(routeStorage + 'before').get_url(None)
        urlAfter = storage.child(routeStorage + 'after').get_url(None)

        #deleteTemporaryImage(images['url-local-images'])
        return { 'message': 'success', 'before': urlBefore, 'after': urlAfter }
    except:
        return { 'message': 'success', 'error': True}


def getTaskBy(searchBy, name):
    return 'Return all tasks'


def getTasks():
    try:
        tasks = db.child('tasks').get()
        return tasks
    except:
        return 'Error al obtner las tareas'


def getHours():
    try:
        hours = []
        hourData = {
            'hours': '',
            'name': '',
            'turn': '',
            'taskType': ''
        }
        hour = 0
        tasks = getFinishedTasks()['tasks']

        for task in tasks:
            hourData['hours'] = task['hour_man']
            hourData['name'] = task['name']
            hourData['turn'] = task['turn']
            hourData['taskType'] = task['type']

            # hours.append(task['hour_man'])
            sum = str(datetime.strptime(task['hour_man'], '%H:%M') + timedelta(hours=hour))[11:19]
            hour += hourToDecimal(task['hour_man'])
            hours.append(hourData)
            hourData = {}

        return { 'hours' : hours, 'suma_de_horas': sum}
    except:
        return 'No ha tareas finalizadas'


def hourToDecimal(hour):
    try:
        h = int(hour[0:2])
        m = int(hour[3:5])

        return float(h + float(m/60))

    except:
        return 'Hora no valida'


def filterTaskBy(tasks, type):
    filter = []
    for task in tasks:
        if task['type'] == type:
            filter.append(task)

    return filter


def getHoursBy(typeTask):

    try:
        hours = []
        hour = 0
        tasks = getFinishedTasks()['tasks']
        myFilter = filterTaskBy(tasks, typeTask)

        for task in myFilter:
            hours.append(task['hourMan'])
            sum = str(datetime.strptime(task['hourMan'], '%H:%M') + timedelta(hours=hour))[11:19]
            hour += hourToDecimal(task['hourMan'])

        return { 'hours' : hours, 'suma_de_horas': sum, 'tasks': myFilter}
    except:
        return 'No ha tareas finalizadas'
