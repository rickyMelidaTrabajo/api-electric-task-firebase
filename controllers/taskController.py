from config import firebase
db = firebase.database()


def getPendingTasks():
    tasks = []
    try:
        pendingTasks = db.child('tasks').child('pending-tasks').get()
        for task in pendingTasks.each():
            tasks.append(task.val())
        print(tasks)
        return {'tasks': tasks}
    except:
        return 'No ha tareas pendientes'


def getFinishedTasks():
    try:
        tasks = []
        finishedTasks = db.child('tasks').child('finished-tasks').get()
        for task in finishedTasks:
            tasks.append(task.val())
        return {'tasks': tasks}
    except:
        return 'No ha tareas finalizadas'


def setPendingTask(data):
    try:
        db.child('tasks').child('pending-tasks').push(data)
        return 'Se ha agregado correctamente la tarea'
    except:
        return 'No se pudo agregar la tarea'


def setFinishedTask(data):
    try:
        db.child('tasks').child('finished-tasks').push(data)
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
