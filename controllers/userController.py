import hashlib
import uuid
from config import firebase
db = firebase.database()
import json
from controllers import authController

def getUser(id):
    usr = {}
    try:
        userDB = db.child('users').child(id).get()

        for user in userDB.each():
            usr[user.key()] = user.val()

        return {'res': usr, 'existUser': True}
    except:
        return {'res': 'No existe el usuario', 'existUser': False}


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

        data['password'] = hashPass
        del data['checkPassword']

        userDB = db.child('users').child(data['_id']).set(data)

        return {'userDB': userDB, 'message': 'Usuario Registrado Correctamente.'}
    except:
        return {'message': 'Error al guardar en la Base de datos'}


def deleteUser(id):
    try:
        user = db.child('users').child(id).remove()

        return { 'message': 'Se ha eliminado el tecnico usuario', 'user': user }
    except:
        return {'message': 'Error al eliminar el tecnico'}


def deleteUserByUsername(username):
    return 'Esto deberia deberia de eliminar un usuario pero por su id'


def updateUser(newData):
    h = hashlib.new('sha1')
    h.update(bytes(newData['password'], 'utf-8'))
    hashPass = h.hexdigest()

    newData['password'] = hashPass
    del newData['checkPassword']

    try:
        update = db.child('users').child(newData['_id']).update(newData)
        return {'message': 'Se modifica el usuario', 'res': update}
    except Exception as e:
        return {'message': 'Error al modificar usuario'}
