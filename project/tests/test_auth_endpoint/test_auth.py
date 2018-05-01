# project/tests/test_auth_endpoint/test_auth.py
"""This module tests the auth blueprint"""

import json
import unittest
from project.server import DB
from project.server.auth.models import User
from project.tests.base import BaseTestCase


def register_user(self, user_level, first_name, last_name, email, password):
    """Register method"""
    return self.client.post(
        '/v1/auth/register',
        data=json.dumps(dict(
            user_level=user_level,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )),
        content_type='application/json',
    )


class TestAuthBlueprint(BaseTestCase):
    """Class containing methods to test various cases in the auth blueprint"""

    def test_registration(self):
        """ Test for user successful registration """
        with self.client:
            response = register_user(
                self, 2, 'Dan', 'Lok', 'joe@gmail.com', 'aaaAAA111')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully registered.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_existing_email_register(self):
        """ Test registration with already registered email"""
        user = User(
            user_level=2,
            first_name='Dan',
            last_name='Lok',
            email='joe@gmail.com',
            password='aaaAAA111'
        )
        DB.session.add(user)
        DB.session.commit()
        with self.client:
            response = register_user(
                self, 2, 'Dan', 'Lok', 'joe@gmail.com', 'aaaAAA111')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(
                data['message'] == 'Email already exists. Please Log in instead.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 202)


if __name__ == '__main__':
    unittest.main()
