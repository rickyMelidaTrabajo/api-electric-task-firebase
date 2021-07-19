from config import firebase
db = firebase.database()


def getPendingTasks():

    return 'I am in getPendingTask method'


def getFinishedTasks():
    return 'Return all the tasks finalize'


def setPendingTask():
    return 'Add new pending task'


def setFinishedTask():
    return 'Add new finished task'


def getTaskBy(searchBy, name):
    return 'Return task by type'


def getTasks():
    return 'Return all tasks'


def getHoursBy(typeTask):
    return 'Return hour by task type'
