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

from swagger_client.models.label import Label  # noqa: F401,E501
from swagger_client.models.paging import Paging  # noqa: F401,E501


class PageableLabelList(object):
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
        'labels': 'list[Label]',
        'paging': 'Paging'
    }

    attribute_map = {
        'labels': 'labels',
        'paging': 'paging'
    }

    def __init__(self, labels=None, paging=None):  # noqa: E501
        """PageableLabelList - a model defined in Swagger"""  # noqa: E501

        self._labels = None
        self._paging = None
        self.discriminator = None

        self.labels = labels
        self.paging = paging

    @property
    def labels(self):
        """Gets the labels of this PageableLabelList.  # noqa: E501

        Data of labels  # noqa: E501

        :return: The labels of this PageableLabelList.  # noqa: E501
        :rtype: list[Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this PageableLabelList.

        Data of labels  # noqa: E501

        :param labels: The labels of this PageableLabelList.  # noqa: E501
        :type: list[Label]
        """
        if labels is None:
            raise ValueError("Invalid value for `labels`, must not be `None`")  # noqa: E501

        self._labels = labels

    @property
    def paging(self):
        """Gets the paging of this PageableLabelList.  # noqa: E501

        Information for pagination  # noqa: E501

        :return: The paging of this PageableLabelList.  # noqa: E501
        :rtype: Paging
        """
        return self._paging

    @paging.setter
    def paging(self, paging):
        """Sets the paging of this PageableLabelList.

        Information for pagination  # noqa: E501

        :param paging: The paging of this PageableLabelList.  # noqa: E501
        :type: Paging
        """
        if paging is None:
            raise ValueError("Invalid value for `paging`, must not be `None`")  # noqa: E501

        self._paging = paging

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
        if not isinstance(other, PageableLabelList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
