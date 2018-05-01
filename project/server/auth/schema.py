# project/server/auth/schema.py
"""Contains the schema for the auth endpoint"""

from marshmallow import Schema, fields, post_load
from project.server.auth.models import User


class UserSchema(Schema):
    """User schema"""
    user_id = fields.Int(dump_only=True)
    user_level = fields.Int()
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    email = fields.Email(required=True)
    password = fields.Str(required=True)
    registered_on = fields.DateTime(dump_only=True)

    @post_load
    def make_user(self, data):
        """Receives dictionary of deserialized data"""
        return User(**data)
