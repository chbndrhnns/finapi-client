# coding: utf-8

"""
    finAPI RESTful Services

    finAPI RESTful Services  # noqa: E501

    OpenAPI spec version: v1.41.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.mandator_administration_api import MandatorAdministrationApi  # noqa: E501
from swagger_client.rest import ApiException


class TestMandatorAdministrationApi(unittest.TestCase):
    """MandatorAdministrationApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.mandator_administration_api.MandatorAdministrationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_users(self):
        """Test case for delete_users

        Delete users  # noqa: E501
        """
        pass

    def test_get_user_list(self):
        """Test case for get_user_list

        Get user list  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
