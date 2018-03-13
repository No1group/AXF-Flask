from flask import Flask

from App import settings
from App.ext import init_ext
from App.views.view_cart import init_cartbp
from App.views.view_home import init_homebp
from App.views.view_market import init_marketbp
from App.views.view_mine import init_minebp


def create_app(env):
    app = Flask(__name__)
    app.config.from_object(settings.env.get(env))
    init_ext(app)
    init_homebp(app)
    init_marketbp(app)
    init_cartbp(app)
    init_minebp(app)
    return app
