# project/server/__init__.py
"""App entry file"""

import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

APP = Flask(__name__)
CORS(APP)

APP_SETTINGS = os.getenv(
    'APP_SETTINGS',
    'project.server.config.DevelopmentConfig'
)
APP.config.from_object(APP_SETTINGS)

BCRYPT = Bcrypt(APP)
DB = SQLAlchemy(APP)
