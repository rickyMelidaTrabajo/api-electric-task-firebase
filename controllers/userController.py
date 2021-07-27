import hashlib
from config import firebase
db = firebase.database()


def getUser(id):
    usr = {}
    try:
        userDB = db.child('users').child(id).get()

        for user in userDB:
            usr[user.key()] = user.val()

        return usr
    except:
        return 'No existe el usuario'


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
    register = firebase.auth()
    try:
        user = register.create_user_with_email_and_password(
            data['email'], data['password'])

        h = hashlib.new('sha1')
        h.update(bytes(data['password'], 'utf-8'))

        data['password'] = h.hexdigest()
        data['checkPassword'] = h.hexdigest()

        userDB = db.child('users').child(user['localId']).set(data)

        return {'user': user, 'userDB': userDB, 'message': 'Se ha creado un nuevo usuario'}
    except:
        return 'El usuario o email ya existe'
