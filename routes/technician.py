from controllers import technicianController
from flask import request


def technician(app, url):

    @app.route(url+'get-technician', methods=['GET'])
    def getTechnician():
        try:
            id = request.args.get('id');
            return technicianController.getTechnician(id)
        except:
            return {'message' : 'Error al recibir parametro de tecnico'}
        return 'this is apart route of technician'

    @app.route(url+'get-technicians', methods=['GET'])
    def getTechnicians():
        username = request.cookies.get('user')
        try:
            return technicianController.getTechnicians()
        except:
            return 'Error al extraer los tecnicos'

    @app.route(url+'set-technician', methods=['GET', 'POST'])
    def setTechnician():
        dataTech = {
            'username': '',
            'name': '',
            'position': '',
            'turn': ''
        }

        try:
            if request.method == 'POST':
                request_data = request.get_json()
                try:
                    for data in dataTech:
                        dataTech[data] = request.form[data]
                except:
                    for data in dataTech:
                        dataTech[data] = request_data[data]

            return technicianController.setTechnician(dataTech)
        except:
            return 'Error al agregar tecnico'

    @app.route(url+'delete-technician', methods=['GET', 'DELETE'])
    def deleteTechnician():
        try:
            id = request.args.get("id")
            return technicianController.deleteTechnician(id)
        except:
            return {'message': 'Error al recibir el parametro'}

    @app.route(url+'update-technician', methods=['GET', 'POST', 'PUT'])
    def updateTechnician():
        dataTech = {
            'username': '',
            'name': '',
            'position': '',
            'turn': ''
        }
        try:
            newData = request.get_json()

            for myData in dataTech:
                dataTech[myData] = newData[myData]

            return technicianController.updateTechnician(dataTech)
        except:
            return {'message': 'Error al extraer los datos a modificar'}
