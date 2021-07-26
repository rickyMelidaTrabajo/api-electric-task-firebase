from controllers import userController
from flask import request
import crypt


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
            'checkPassword':'',
            'rol': ''
        }

        if request.method == 'POST':
            for usr in dataUsers:
                dataUsers[usr] = request.form[usr]
        try:
            if dataUsers['password'] == dataUsers['checkPassword']:
                dataUsers['password'] = crypt.crypt(request.form['password'], 'taks')
                dataUsers['checkPassword'] = crypt.crypt(request.form['checkPassword'], 'taks')
            
                return userController.setUser(dataUsers)
            else:
                return 'Las contraseñas no coinciden'

        except:
            return 'Error al agregar nuevo usuario'
