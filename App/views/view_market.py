from flask import Blueprint

marketbp = Blueprint("marketbp", __name__)


def init_marketbp(app):
    app.register_blueprint(blueprint=marketbp)


@marketbp.route('/')
def index():
    return 'hh'