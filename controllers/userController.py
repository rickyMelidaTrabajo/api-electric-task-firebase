from config import firebase
db = firebase.database()


def getUser(id):
    return 'Return only one username'


def getUsers():
    users = []
    try:
        usrs = db.child('users').get()
        for usr in usrs:
            users.append(usr.val())
        return {'users': users}
    except:
        return 'Error al extraer los usuarios'


def setUser(data):
    try:
        db.child('users').push(data)
        return 'Add new user'
    except:
        return 'Error al agregar usuario'
