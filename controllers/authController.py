from config import firebase
from flask import make_response
from controllers import userController
import hashlib

def sigin(email, password):
    login = firebase.auth()

    try:
        loginUser = login.sign_in_with_email_and_password(email, password)
        tech = userController.getUser(loginUser['localId'])
        cookie = make_response({'username': tech['username'], 'message': 'Te has logueado correctamente', 'status': 200 , 'token': loginUser['refreshToken']})
        cookie.delete_cookie('user')
        cookie.set_cookie('user', tech['username'])

        return cookie
    except:
        return 'Email o password incorrecto'


def signinAdmin(username, password):
    db = firebase.database()

    h = hashlib.new('sha1')
    h.update(bytes(password, 'utf-8'))
    passwordHash = h.hexdigest()

    adminUser = {
    'username': '',
    'email': ''
    }

    try:
        usrs = db.child('users').get()
        for user in usrs.each():
            if user.val()['password'] == passwordHash and user.val()['username'] == username and user.val()['rol'] == 'Admin':
                adminUser['username'] = user.val()['username']
                adminUser['email'] = user.val()['email']

        return sigin(adminUser['email'], password)

    except:
        return {'message': 'Error al obtener los usuarios', 'status': 400 }


def sigup(userData):
    register = firebase.auth()

    if userData['password'] == userData['passwordCheck']:
        try:
            usr = register.create_user_with_email_and_password(userData['email'], userData['password'])
            userData['_id'] = usr['localId']

            return userController.setUser(userData)
        except:
            return 'Email ya esta registrado'
    else:
        return 'Las contrasenas no coinciden'


def verifyToken(token):
    login = firebase.auth()

    try:
        verifyToken = login.refresh(token)
        user = userController.getUser(verifyToken['userId'])

        return {'user': user, 'message': 'Token validado correctamente.'}
    except:
        return {'message': 'Token invalido'}


def verifyAdminToken(token):
    return 'Verify admin token'
