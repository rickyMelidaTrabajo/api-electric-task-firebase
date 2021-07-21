from controllers import technicianController
from flask import request


def technician(app, url):

    @app.route(url+'get-technician', methods=['GET'])
    def getTechnician():
        return 'this is apart route of technician'

    @app.route(url+'get-technicians', methods=['GET'])
    def getTechnicians():
        try:
            return technicianController.getTechnicians()
        except:
            return 'This is the getTechnicians route'

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
                for data in dataTech:
                    dataTech[data] = request.form[data]

            technicianController.setTechnician(dataTech)
            return 'Se ha agregado el tecnico correctamente'
        except:
            return 'Error al agregar tecnico'
