# project/tests/test_auth_endpoint/test_auth.py
"""This module tests the auth blueprint"""

import json
import unittest
from project.server import DB
from project.server.auth.models import User
from project.tests.base import BaseTestCase


def register_user(self, first_name, last_name, email, password):
    """Register method"""
    return self.client.post(
        '/v1/auth/register',
        data=json.dumps(dict(
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
                self, 'Dan', 'Lok', 'joe@gmail.com', 'aaaAAA111')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'success')
            self.assertTrue(data['message'] == 'Successfully registered.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_existing_email_register(self):
        """ Test registration with already registered email"""
        user = User(
            first_name='Dan',
            last_name='Lok',
            email='joe@gmail.com',
            password='aaaAAA111'
        )
        DB.session.add(user)
        DB.session.commit()
        with self.client:
            response = register_user(
                self, 'Dan', 'Lok', 'joe@gmail.com', 'aaaAAA111')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(
                data['message'] ==
                'Email already exists. Please Log in instead.'
            )
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 202)

    def test_check_for_no_input(self):
        """Check if only value entered is {}"""
        response = self.client.post(
            '/v1/auth/register',
            data=json.dumps({}),
            content_type='application/json'
        )
        result = json.loads(response.data)
        self.assertEqual(result["status"], "fail")
        self.assertEqual(result["message"], "No input data provided.")
        self.assertEqual(response.status_code, 400)

    def test_return_validation_error(self):
        """Test if validation error is returned"""
        with self.client:
            response = register_user(
                self, 'Dan', 'Lok', 'joegmailom', 'aaaAAA111')
            data = json.loads(response.data.decode())
            self.assertTrue(data['status'] == 'fail')
            self.assertTrue(data['message'] == 'Validation errors.')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 422)


if __name__ == '__main__':
    unittest.main()
