from flask_cache import Cache
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension

models = SQLAlchemy()
migrate = Migrate()
# debugtoolbar = DebugToolbarExtension()
# cache = Cache(
#     config={"CACHE_TYPE":"redis"}
# )


def init_ext(app):
    models.init_app(app=app)
    migrate.init_app(app=app, db=models)

    # cache.init_app(app=app)
    # debugtoolbar.init_app(app=app)