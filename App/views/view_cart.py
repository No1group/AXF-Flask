from flask import Blueprint

cartbp = Blueprint("cartbp", __name__)


def init_cartbp(app):
    app.register_blueprint(blueprint=cartbp)


@cartbp.route('/cart/')
def index():
    return 'hh'