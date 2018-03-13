from flask import Blueprint

homebp = Blueprint("homebp", __name__)


def init_homebp(app):
    app.register_blueprint(blueprint=homebp)

@homebp.route('/')
def index():
    return 'hh'