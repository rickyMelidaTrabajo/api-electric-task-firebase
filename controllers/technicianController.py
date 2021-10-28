from config import firebase
from flask.globals import request

db = firebase.database()


def getTechnician(id):
    techById = {}
    try:
        technician = db.child('technicians').child(id).get()
        for tech in technician.each():
            techById[tech.key()] = tech.val()

        return {'message': 'succes', 'technician': techById}
    except:
        return {'message': 'Error al extraer tecnico'}


def getTechnicians():
    techs = []
    ids = []
    index = 0
    try:
        technicians = db.child('technicians').get()
        for tech in technicians.each():
            techs.append(tech.val())
            ids.append(tech.key())

        for t in techs:
            t['_id'] = ids[index]
            index = index+1

        return {'techs': techs}
    except:
        return 'Error al obtener los tecnicos'


def setTechnician(data):
    try:
        technician = db.child('technicians').push(data)
        return {'message': 'Se ha agregado el tecnico correctamente', 'technician': technician}
    except:
        return 'Error al agregar tecnico'


def getWithUsername(username):
    techs = []
    try:
        technicians = db.child('technicians').get()
        for tech in technicians.each():
            if tech.val()['username'] == username:
                techs.append(tech.val())

        return {'techs': techs}
    except:
        return 'Error al obtener los tecnicos'


def getWithEmail(email):
    return 'Return technician with your username'


def getHours():
    return 'Return hours total from technician'

def deleteTechnician(id):
    try:
        technician = db.child('technicians').child(id).remove()

        return { 'message': 'Se ha eliminado el tecnico correctamente', 'tech': technician }
    except:
        return {'message': 'Error al eliminar el tecnico'}

def updateTechnician(newData):
    try:
        update = db.child('technicians').child(newData['_id']).update(newData)
        return {'message': 'Se ha modificado el tecnico', 'res': update}
    except:
        return {'message': 'Error al modificar el tecnico'}
