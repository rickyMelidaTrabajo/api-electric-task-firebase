from .technician import technician
from .user import user
from .task import task
from .auth import auth


def route(app):
    technician(app, '/api/technician/')
    user(app, '/api/user/')
    task(app, '/api/task/')
    auth(app, '/api/auth/')
