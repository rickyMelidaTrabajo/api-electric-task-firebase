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
            'checkPassword':'',
            'rol': '',
            '_id':''
        }

        if request.method == 'POST':
            request_data = request.get_json()
            try:
                for usr in dataUsers:
                    dataUsers[usr] = request.form[usr]
            except:
                for data in dataUsers:
                    dataUsers[data] = request_data[data]

            if dataUsers['password'] == dataUsers['checkPassword']:
                return userController.setUser(dataUsers)
            else:
                return 'Las contraseñas no coinciden'

            return 'Error al agregar nuevo usuario'

    @app.route(url+'delete-user', methods=['GET', 'POST', 'DELETE'])
    def deleteUserByUsername():
        try:
            id = request.args.get("id")
            return userController.deleteUser(id)
        except:
            return {'message': 'Error al recibir el parametro'}

    @app.route(url+'update-user', methods=['GET', 'PUT', 'POST'])
    def updateUser():
        dataUsers = {
            'username': '',
            'email': '',
            'password': '',
            'checkPassword':'',
            'rol': '',
            '_id':''
        }
        try:
            newData = request.get_json()

            for myData in dataUsers:
                dataUsers[myData] = newData[myData]

            return userController.updateUser(dataUsers)
        except Exception as e:
            return {'message': 'Error al extraer los datos a modificar'}
