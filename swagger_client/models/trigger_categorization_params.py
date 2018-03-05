# coding: utf-8

"""
    finAPI RESTful Services

    finAPI RESTful Services  # noqa: E501

    OpenAPI spec version: v1.41.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TriggerCategorizationParams(object):
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
        'bank_connection_ids': 'list[int]'
    }

    attribute_map = {
        'bank_connection_ids': 'bankConnectionIds'
    }

    def __init__(self, bank_connection_ids=None):  # noqa: E501
        """TriggerCategorizationParams - a model defined in Swagger"""  # noqa: E501

        self._bank_connection_ids = None
        self.discriminator = None

        if bank_connection_ids is not None:
            self.bank_connection_ids = bank_connection_ids

    @property
    def bank_connection_ids(self):
        """Gets the bank_connection_ids of this TriggerCategorizationParams.  # noqa: E501

        List of identifiers of the bank connections that you want to trigger categorization for. Leaving the list unset or empty will trigger categorization for all of the user's bank connections. Please note that if there are no bank connections, then the service will return with HTTP code 422.  # noqa: E501

        :return: The bank_connection_ids of this TriggerCategorizationParams.  # noqa: E501
        :rtype: list[int]
        """
        return self._bank_connection_ids

    @bank_connection_ids.setter
    def bank_connection_ids(self, bank_connection_ids):
        """Sets the bank_connection_ids of this TriggerCategorizationParams.

        List of identifiers of the bank connections that you want to trigger categorization for. Leaving the list unset or empty will trigger categorization for all of the user's bank connections. Please note that if there are no bank connections, then the service will return with HTTP code 422.  # noqa: E501

        :param bank_connection_ids: The bank_connection_ids of this TriggerCategorizationParams.  # noqa: E501
        :type: list[int]
        """

        self._bank_connection_ids = bank_connection_ids

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
        if not isinstance(other, TriggerCategorizationParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
