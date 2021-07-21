from config import firebase

db = firebase.database()


def getTechnician(id):
    return 'Return only one tech'


def getTechnicians():
    techs = []
    try:
        technicians = db.child('technicians').get()
        for tech in technicians.each():
            techs.append(tech.val())

        return {'techs': techs}
    except:
        return 'Error al obtener los tecnicos'


def setTechnician(data):
    try:
        db.child('technicians').push(data)
        return 'Se ha agregado el tecnico correctamente'
    except:
        return 'Error al agregar tecnico'


def getWithUsername(username):
    return 'Return technician with your username'


def getHours():
    return 'Return hours total from technician'
