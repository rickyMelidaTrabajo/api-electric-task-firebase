from .technician import technician
from .user import user
from .task import task
from .auth import auth


def route(app):
    technician(app, '/technician/')
    user(app, '/user/')
    task(app, '/task/')
    auth(app, '/auth/')
