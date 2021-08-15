def getNumberTasks(db):
    try:
        return int(getNumberPendingTask(db)) + int(getNumberFinishedTask(db))
    except:
        return 'Error al obtener la cantidad total de tareas'


def getNumberPendingTask(db):
    tasks = []
    try:
        taskPending = db.child('tasks').child('pending-tasks').get()
        for task in taskPending.each():
            tasks.append(task.val())

        print(f'la cantidad de tareas pendientes es: {len(tasks)}')
        return len(tasks)
    except:
        return 0
        

def getNumberFinishedTask(db):
    tasks = []
    try:
        taskPending = db.child('tasks').child('finished-tasks').get()
        for task in taskPending.each():
            tasks.append(task.val())

        print(f'la cantidad de tareas finalizadas es: {len(tasks)}')
        return len(tasks)
    except:
        return 0

