from controllers import authController
from flask import request


def auth(app, url):

    @app.route(url+'sigin', methods=['GET', 'POST'])
    def sigin():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']

            return authController.sigin(email, password)
        else:
            return 'This is signin route'

    @app.route(url+'sigup', methods=['GET', 'POST'])
    def sigup():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            passwordCheck = request.form['password-check']

            return authController.sigup(email, password, passwordCheck)
        else:
            return 'This is sigup route'

    @app.route(url+'token-verify', methods=['GET', 'POST'])
    def tokenValidate():
        return 'This is tokenValidate route'

    @app.route(url+'admin-token-validate', methods=['GET', 'POST'])
    def adminTokenValidate():
        return 'This is adminTokenValidate route'
