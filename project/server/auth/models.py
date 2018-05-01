# project/server/auth/models.py
"""Database models for the auth endpoint"""

import datetime
from project.server import APP, DB, BCRYPT


class User(DB.Model):  # pylint: disable=too-few-public-methods
    """ User Model for storing user related details """
    __tablename__ = "tbl_users"

    user_id = DB.Column(DB.Integer, primary_key=True, autoincrement=True)
    user_level = DB.Column(DB.Integer)
    first_name = DB.Column(DB.String(50), nullable=False)
    last_name = DB.Column(DB.String(50), nullable=False)
    email = DB.Column(DB.String(255), unique=True, nullable=False)
    password = DB.Column(DB.String(255), nullable=False)
    registered_on = DB.Column(DB.DateTime, nullable=False)

    def __init__(self, user_level, first_name, last_name, email, password):
        self.user_level = user_level
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = BCRYPT.generate_password_hash(
            password, APP.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()
        self.registered_on = datetime.datetime.now()
