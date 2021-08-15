from controllers import authController
from flask import request


def auth(app, url):

    @app.route(url+'signin', methods=['GET', 'POST'])
    def sigin():

        if request.method == 'POST':
            request_data = request.get_json()

            try:
                email = request.form['email']
                password = request.form['password']
            except:
                email = request_data['email']
                password = request_data['password']

            return authController.sigin(email, password)
        else:
            return 'Faltan completar datos'


    @app.route(url+'signin-admin', methods=['GET', 'POST'])
    def signinAdmin():
        if request.method == 'POST':
            request_data = request.get_json()

            try:
                username = request.form['username']
                password = request.form['password']
            except:
                username = request_data['username']
                password = request_data['password']

            return authController.signinAdmin(username, password)
        else:
            return 'Faltan completar datos'


    @app.route(url+'signup', methods=['GET', 'POST'])
    def sigup():
        if request.method == 'POST':
            request_data = request.get_json()
            userData = {
                '_id': '',
                'email': '',
                'password': '',
                'passwordCheck': '',
                'rol': 'Usuario',
                'username': ''
            }

            try:
                userData['email'] = request.form['email']
                userData['password'] = request.form['password']
                userData['passwordCheck'] = request.form['password-check']
                userData['username'] = request.form['username']
            except:
                userData['email'] = request_data['email']
                userData['password'] = request_data['password']
                userData['passwordCheck'] = request_data['password-check']
                userData['username'] = request_data['username']

            return authController.sigup(userData)
        else:
            return 'Error al registrar usuario'

    @app.route(url+'token-verify', methods=['GET', 'POST'])
    def tokenValidate():
        try:
            token = request.args.get('token')
            return authController.verifyToken(token)
        except:
            return 'Error get token'

    @app.route(url+'admin-token-validate', methods=['GET', 'POST'])
    def adminTokenValidate():
        return 'This is adminTokenValidate route'
