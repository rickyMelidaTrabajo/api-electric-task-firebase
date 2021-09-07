import hashlib
import uuid
from config import firebase
db = firebase.database()


def getUser(id):
    usr = {}
    try:
        userDB = db.child('users').child(id).get()

        for user in userDB.each():
            usr[user.key()] = user.val()

        return usr
    except:
        return 'No existe el usuario'


def getUsers():
    users = []

    try:
        usrs = db.child('users').get()
        for usr in usrs.each():
            users.append(usr.val())

        return {'users': users}
    except:
        return 'Error al extraer los usuarios'


def setUser(data):
    try:
        h = hashlib.new('sha1')
        h.update(bytes(data['password'], 'utf-8'))
        hashPass = h.hexdigest()
        data['_id'] = uuid.uuid1().hex


        data['password'] = hashPass
        del data['checkPassword']

        userDB = db.child('users').child(data['_id']).set(data)

        return {'userDB': userDB, 'message': 'Se ha creado un nuevo usuario'}
    except:
        return {'message': 'Error al guardar en la Base de datos'}
