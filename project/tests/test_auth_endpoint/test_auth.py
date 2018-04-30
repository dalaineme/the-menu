# project/tests/test_auth_endpoint/test_auth.py
"""This module tests the auth blueprint"""

import json
import unittest
from project.tests.base import BaseTestCase


class TestAuthBlueprint(BaseTestCase):
    """Class containing methods to test various cases in the auth blueprint"""

    def test_display_hello_world(self):
        """ Test for printing out hello world """
        response = self.client.get('/auth/register')
        result = json.loads(response.data)
        self.assertEqual(result["message"], "hello world")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
