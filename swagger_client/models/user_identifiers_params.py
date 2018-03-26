# coding: utf-8

"""
    finAPI RESTful Services

    finAPI RESTful Services  # noqa: E501

    OpenAPI spec version: v1.42.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class UserIdentifiersParams(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'user_ids': 'list[str]'
    }

    attribute_map = {
        'user_ids': 'userIds'
    }

    def __init__(self, user_ids=None):  # noqa: E501
        """UserIdentifiersParams - a model defined in Swagger"""  # noqa: E501

        self._user_ids = None
        self.discriminator = None

        self.user_ids = user_ids

    @property
    def user_ids(self):
        """Gets the user_ids of this UserIdentifiersParams.  # noqa: E501

        List of user identifiers  # noqa: E501

        :return: The user_ids of this UserIdentifiersParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._user_ids

    @user_ids.setter
    def user_ids(self, user_ids):
        """Sets the user_ids of this UserIdentifiersParams.

        List of user identifiers  # noqa: E501

        :param user_ids: The user_ids of this UserIdentifiersParams.  # noqa: E501
        :type: list[str]
        """
        if user_ids is None:
            raise ValueError("Invalid value for `user_ids`, must not be `None`")  # noqa: E501

        self._user_ids = user_ids

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UserIdentifiersParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
