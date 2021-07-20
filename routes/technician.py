from controllers import technicianController
from flask import request

def technician(app, url):

    @app.route(url+'get-technician', methods=['GET'])
    def getTechnician():
        return 'this is apart route of technician'

    @app.route(url+'get-technicians', methods=['GET'])
    def getTechnicians():
        return 'This is the getTechnicians route'

    @app.route(url+'set-technician', methods=['GET', 'POST'])
    def setTechnician():
        data = {}
        if request.method == 'POST':
            name = request.form['name']
            position = request.form['position']
            turn = request.form['turn']
            
            data['name'] = name
            data['position'] = position
            data['turn'] = turn
        try:
            technicianController.setTechnician(data)
            return 'Se ha agregado el tecnico correctamente'
        except:
            return 'Error al agregar tecnico'

