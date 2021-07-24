from config import firebase
import uuid
import controllers.numberTasks as TaskNumber
import controllers.technicianController as Technician
from datetime import datetime
db = firebase.database()


def getPendingTasks():
    tasks = []
    try:
        pendingTasks = db.child('tasks').child('pending-tasks').get()
        for task in pendingTasks.each():
            tasks.append(task.val())
        return { 'tasks': tasks }
    except:
        return 'No hay tareas pendientes'


def getFinishedTasks():
    try:
        tasks = []
        finishedTasks = db.child('tasks').child('finished-tasks').get()
        for task in finishedTasks:
            tasks.append(task.val())
        return {'tasks': tasks, 'lenght': len(tasks)}
    except:
        return 'No ha tareas finalizadas'


def setPendingTask(dataForm):
    _id = uuid.uuid1().hex
    taskNumber = TaskNumber.getNumberTasks(db) + 1
    dateGeneration = datetime.now().strftime('%d-%m-%Y')

    try:
        db.child('tasks').child('pending-tasks').push(dataForm)
        return {'message' : 'Se ha agregado correctamente la tarea', 'taskNumber': taskNumber}
    except:
        return 'No se pudo agregar la tarea'


def setFinishedTask(dataForm):
    try:
        db.child('tasks').child('finished-tasks').push(dataForm)
        return 'Se ha agregado correctamente la tarea'
    except:
        return 'No se pudo agregar la tarea'


def getTaskBy(searchBy, name):
    return 'Return all tasks'


def getTasks():
    try:
        tasks = db.child('tasks').get()
        return tasks
    except:
        return 'Error al obtner las tareas'


def getHoursBy(typeTask):
    return 'Return hour by task type'
