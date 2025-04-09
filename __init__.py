

package __init__

from . import config
from . import models
from . import routes
from . import services
from . import utils

def init_app(app):
    config.init_app(app)
    models.init_app(app)
    routes.init_app(app)
    services.init_app(app)
    utils.init_app(app)

def init_db():
    models.init_db()

def init_services():
    services.init_services()

__all__ = ['init_app', 'init_db', 'init_services', 'config', 'models', 'routes', 'services', 'utils']