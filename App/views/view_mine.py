from flask import Blueprint

minebp = Blueprint("minebp", __name__)


def init_minebp(app):
    app.register_blueprint(blueprint=minebp)


@minebp.route('/')
def index():
    return 'hh'