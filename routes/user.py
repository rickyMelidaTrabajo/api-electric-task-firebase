from controllers import userController
from flask import request


def user(app, url):
    @app.route(url+'get-user', methods=['GET'])
    def getUser():
        return 'This is getUSer route'

    @app.route(url+'get-users', methods=['GET'])
    def getUsers():
        try:
            return userController.getUsers()
        except:
            return 'This is getUsers route'

    @app.route(url+'set-user', methods=['GET', 'POST'])
    def setUser():
        dataUsers = {
            'username': '',
            'email': '',
            'password': '',
            'rol': ''
        }

        if request.method == 'POST':
            for usr in dataUsers:
                dataUsers[usr] = request.form[usr]
        try:
            userController.setUser(dataUsers)
            return 'Se ha agregado usuario correctamente'
        except:
            return 'Error al agregar nuevo usuario'
