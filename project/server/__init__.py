# project/server/__init__.py
"""App entry file"""

import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flasgger import Swagger, APISpec


APP = Flask(__name__)
CORS(APP)

APP_SETTINGS = os.getenv(
    'APP_SETTINGS',
    'project.server.config.DevelopmentConfig'
)
APP.config.from_object(APP_SETTINGS)

BCRYPT = Bcrypt(APP)
DB = SQLAlchemy(APP)
SWAG = Swagger(
    APP,
    template={
        "openapi": "3.0.0",
        "info": {
            "title": "The Menu API - Docs",
            "version": "1.0",
        },
        "consumes": [
            "application/x-www-form-urlencoded",
        ],
        "produces": [
            "application/json",
        ],
    },
)


from project.server.auth.views import AUTH_BLUEPRINT  # nopep8  # pylint: disable=C0413

APP.register_blueprint(AUTH_BLUEPRINT)
