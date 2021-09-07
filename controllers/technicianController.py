from config import firebase
from flask.globals import request

db = firebase.database()


def getTechnician(id):
    return 'Return only one tech'


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
            #print(t['name'])

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
