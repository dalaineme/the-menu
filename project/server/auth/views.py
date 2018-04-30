# project/server/auth/views.py
"""This module contains various routes for the auth endpoint"""

from flask import Blueprint, jsonify
from flask.views import MethodView

AUTH_BLUEPRINT = Blueprint('auth', __name__)


class RegisterAPI(MethodView):
    """User Registration resource"""

    def get(self):
        """Get users"""
        return jsonify({'message': 'hello world'}), 200


# define API resources
REGISTRATION_VIEW = RegisterAPI.as_view('register_api')

# add rules for auth enpoints
AUTH_BLUEPRINT.add_url_rule(
    '/auth/register',
    view_func=REGISTRATION_VIEW,
    methods=['GET']
)
