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
        data = {}
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            password = request.form['email']
            rol = request.form['email']

            data['username'] = username
            data['email'] = email
            data['password'] = password
            data['rol'] = rol

        try:
            userController.setUser(data)
            return 'Se ha agregado usuario correctamente'
        except:
            return 'Error al agregar nuevo usuario'