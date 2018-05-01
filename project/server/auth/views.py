# project/server/auth/views.py
"""This module contains various routes for the auth endpoint"""

from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from project.server import DB
from project.server.auth.models import User

AUTH_BLUEPRINT = Blueprint('auth', __name__, url_prefix='/v1/auth')


class RegisterAPI(MethodView):
    """User Registration resource"""

    def post(self):
        """
        file: documentation/register.yml
        """
        # get the post data
        post_data = request.get_json()
        # check if user already exists
        user = User.query.filter_by(email=post_data.get('email')).first()
        if not user:

            user = User(
                user_level=2,
                first_name=post_data.get('first_name'),
                last_name=post_data.get('last_name'),
                email=post_data.get('email'),
                password=post_data.get('password')
            )
            # insert the user
            DB.session.add(user)
            DB.session.commit()

            response_object = {
                'status': 'success',
                'message': 'Successfully registered.'
            }
            return make_response(jsonify(response_object)), 201
        # case email exists
        response_object = {
            'status': 'fail',
            'message': 'Email already exists. Please Log in instead.',
        }
        return make_response(jsonify(response_object)), 202


# define API resources
REGISTRATION_VIEW = RegisterAPI.as_view('register_api')

# add rules for auth enpoints
AUTH_BLUEPRINT.add_url_rule(
    '/register',
    view_func=REGISTRATION_VIEW,
    methods=['POST']
)
