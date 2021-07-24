def getNumberTasks(db):
    try:
        return getNumberPendingTask(db) + getNumberFinishedTask(db)
    except:
        return 'Error al obtener la cantidad total de tareas'


def getNumberPendingTask(db):
    tasks = []
    try:
        taskPending = db.child('tasks').child('pending-tasks').get()
        for task in taskPending.each():
            tasks.append(task.val())

        return len(tasks)
    except:
        return 'Error al obtener la cantidad de tareas pendientes'
        

def getNumberFinishedTask(db):
    tasks = []
    try:
        taskPending = db.child('tasks').child('finished-tasks').get()
        for task in taskPending.each():
            tasks.append(task.val())

        return len(tasks)
    except:
        return 'Error al obtener la cantidad de tareas finalizadas'

