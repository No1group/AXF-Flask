from flask import Blueprint, current_app

from App.ext import models
from App.models.models import BaseMain

homebp = Blueprint("homebp", __name__)


def init_homebp(app):
    app.register_blueprint(blueprint=homebp)

@homebp.route('/')
def index():
    m = BaseMain()
    m.name = 'ssss'
    m.img = 'sss'
    m.trackid = '1'
    models.session.add(m)
    models.session.commit()




    return 'hh0'