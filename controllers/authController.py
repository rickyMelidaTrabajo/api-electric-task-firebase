from config import firebase
from flask import make_response
from controllers import userController


def sigin(email, password):
    login = firebase.auth()

    try:
        cookie = make_response('Usuario autenticado correctamente')

        login = login.sign_in_with_email_and_password(email, password)

        tech = userController.getUser(login['localId'])
        cookie.delete_cookie('user')
        cookie.set_cookie('user', tech['username'])

        return cookie
    except:
        return 'Email o password incorrecto'


def sigup(email, password, checkPassword):
    register = firebase.auth()

    if password == checkPassword:
        try:
            usr = register.create_user_with_email_and_password(email, password)

            return {'users': usr}
        except:
            return 'Email ya esta registrado'
    else:
        return 'Las contrasenas no coinciden'


def verifyToken(token):
    return 'verify users token'


def verifyAdminToken(token):
    return 'Verify admin token'
