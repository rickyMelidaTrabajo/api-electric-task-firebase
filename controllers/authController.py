from config import firebase
from flask import make_response

def sigin(email, password):
    login = firebase.auth()
    try:
        usr = login.sign_in_with_email_and_password(email, password)
        print(usr['email'])
        resp = make_response('Cookie conectada')
        resp.set_cookie('miCookie', 'mi cookie personalizada')

        return 'resp'
    except:
        return 'Email o password incorrecto'


def sigup(email, password, checkPassword):
    register = firebase.auth()

    if password == checkPassword:
        try:
            cre = register.credentials()
            usr = register.create_user_with_email_and_password(email, password)
            print(usr)
            return {'users': usr}
        except:
            return 'Email ya esta registrado'
    else:
        return 'Las contrasenas no coinciden'


def verifyToken(token):
    return 'verify users token'


def verifyAdminToken(token):
    return 'Verify admin token'
