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


class ErrorDetails(object):
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
        'message': 'str',
        'code': 'str',
        'type': 'str'
    }

    attribute_map = {
        'message': 'message',
        'code': 'code',
        'type': 'type'
    }

    def __init__(self, message=None, code=None, type=None):  # noqa: E501
        """ErrorDetails - a model defined in Swagger"""  # noqa: E501

        self._message = None
        self._code = None
        self._type = None
        self.discriminator = None

        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
        if type is not None:
            self.type = type

    @property
    def message(self):
        """Gets the message of this ErrorDetails.  # noqa: E501

        Error message  # noqa: E501

        :return: The message of this ErrorDetails.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ErrorDetails.

        Error message  # noqa: E501

        :param message: The message of this ErrorDetails.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def code(self):
        """Gets the code of this ErrorDetails.  # noqa: E501

        Error code. See the documentation of the individual services for details about what values may be returned.  # noqa: E501

        :return: The code of this ErrorDetails.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ErrorDetails.

        Error code. See the documentation of the individual services for details about what values may be returned.  # noqa: E501

        :param code: The code of this ErrorDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["MISSING_FIELD", "UNKNOWN_ENTITY", "METHOD_NOT_ALLOWED", "ENTITY_EXISTS", "ILLEGAL_ENTITY_STATE", "UNEXPECTED_ERROR", "ILLEGAL_FIELD_VALUE", "UNAUTHORIZED_ACCESS", "BAD_REQUEST", "UNSUPPORTED_ORDER", "ILLEGAL_PAGE_SIZE", "INVALID_FILTER_OPTIONS", "TOO_MANY_IDS", "BANK_SERVER_REJECTION", "IBAN_ONLY_MONEY_TRANSFER_NOT_SUPPORTED", "IBAN_ONLY_DIRECT_DEBIT_NOT_SUPPORTED", "COLLECTIVE_MONEY_TRANSFER_NOT_SUPPORTED", "INVALID_TWO_STEP_PROCEDURE", "MISSING_TWO_STEP_PROCEDURE", "UNSUPPORTED_MEDIA_TYPE", "UNSUPPORTED_BANK", "USER_NOT_VERIFIED", "USER_ALREADY_VERIFIED", "INVALID_TOKEN", "LOCKED", "NO_ACCOUNTS_FOR_TYPE_LIST", "FORBIDDEN", "NO_EXISTING_CHALLENGE", "ADDITIONAL_AUTHENTICATION_REQUIRED"]  # noqa: E501
        if code not in allowed_values:
            raise ValueError(
                "Invalid value for `code` ({0}), must be one of {1}"  # noqa: E501
                .format(code, allowed_values)
            )

        self._code = code

    @property
    def type(self):
        """Gets the type of this ErrorDetails.  # noqa: E501

        Error type. BUSINESS errors depict German error messages for the user, e.g. from a bank server. TECHNICAL errors depict internal errors.  # noqa: E501

        :return: The type of this ErrorDetails.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ErrorDetails.

        Error type. BUSINESS errors depict German error messages for the user, e.g. from a bank server. TECHNICAL errors depict internal errors.  # noqa: E501

        :param type: The type of this ErrorDetails.  # noqa: E501
        :type: str
        """
        allowed_values = ["BUSINESS", "TECHNICAL"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if not isinstance(other, ErrorDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
