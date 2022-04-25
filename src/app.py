from flask import Flask
# from flasgger import Swagger

from .Shared.Providers.db import db
from src.Routes.CustomerRoutes import customers_blueprints


def create_app(app_name='OnlineStore', test_config=False, production_conf=False):
    app = Flask(app_name)

    # app.config['SWAGGER'] = {
    #     "title": "Challenge Shape Backend"
    # }

    # swagger = Swagger(app)

    app.config.from_object('config.RunConfig')

    # Register api blueprints
    app.register_blueprint(customers_blueprints, url_prefix='/customers')

    db.init_app(app)

    return app
