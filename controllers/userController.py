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
        return { 'users': users }
    except:
        return 'Error al extraer los usuarios'

def setUser():
    return 'Add new user'
