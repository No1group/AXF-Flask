from flask_cache import Cache
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

model = SQLAlchemy()
migrate = Migrate()
# cache = Cache(
#     config={"CACHE_TYPE":"redis"}
# )


def init_ext(app):
    model.init_app(app=app)
    migrate.init_app(app=app, db=model)
    # cache.init_app(app)