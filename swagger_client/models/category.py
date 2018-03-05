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


class Category(object):
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
        'id': 'int',
        'name': 'str',
        'parent_id': 'int',
        'parent_name': 'str',
        'is_custom': 'bool',
        'children': 'list[int]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'parent_id': 'parentId',
        'parent_name': 'parentName',
        'is_custom': 'isCustom',
        'children': 'children'
    }

    def __init__(self, id=None, name=None, parent_id=None, parent_name=None, is_custom=False, children=None):  # noqa: E501
        """Category - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._parent_id = None
        self._parent_name = None
        self._is_custom = None
        self._children = None
        self.discriminator = None

        self.id = id
        self.name = name
        if parent_id is not None:
            self.parent_id = parent_id
        if parent_name is not None:
            self.parent_name = parent_name
        self.is_custom = is_custom
        if children is not None:
            self.children = children

    @property
    def id(self):
        """Gets the id of this Category.  # noqa: E501

        Category identifier.<br/><br/>NOTE: Do NOT assume that the identifiers of the global finAPI categories are the same across different finAPI environments. In fact, the identifiers may change whenever a new finAPI version is released, even within the same environment. The identifiers are meant to be used for references within the finAPI services only, but not for hard-coding them in your application. If you need to hard-code the usage of a certain global category within your application, please instead refer to the category name. Also, please make sure to check the 'isCustom' flag, which is false for all global categories (if you are not regarding this flag, you might end up referring to a user-specific category, and not the global category).  # noqa: E501

        :return: The id of this Category.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Category.

        Category identifier.<br/><br/>NOTE: Do NOT assume that the identifiers of the global finAPI categories are the same across different finAPI environments. In fact, the identifiers may change whenever a new finAPI version is released, even within the same environment. The identifiers are meant to be used for references within the finAPI services only, but not for hard-coding them in your application. If you need to hard-code the usage of a certain global category within your application, please instead refer to the category name. Also, please make sure to check the 'isCustom' flag, which is false for all global categories (if you are not regarding this flag, you might end up referring to a user-specific category, and not the global category).  # noqa: E501

        :param id: The id of this Category.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Category.  # noqa: E501

        Category name  # noqa: E501

        :return: The name of this Category.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Category.

        Category name  # noqa: E501

        :param name: The name of this Category.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def parent_id(self):
        """Gets the parent_id of this Category.  # noqa: E501

        Identifier of the parent category (if a parent category exists)  # noqa: E501

        :return: The parent_id of this Category.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this Category.

        Identifier of the parent category (if a parent category exists)  # noqa: E501

        :param parent_id: The parent_id of this Category.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def parent_name(self):
        """Gets the parent_name of this Category.  # noqa: E501

        Name of the parent category (if a parent category exists)  # noqa: E501

        :return: The parent_name of this Category.  # noqa: E501
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        """Sets the parent_name of this Category.

        Name of the parent category (if a parent category exists)  # noqa: E501

        :param parent_name: The parent_name of this Category.  # noqa: E501
        :type: str
        """

        self._parent_name = parent_name

    @property
    def is_custom(self):
        """Gets the is_custom of this Category.  # noqa: E501

        Whether the category is a finAPI global category (in which case this field will be false), or the category was created by a user (in which case this field will be true)  # noqa: E501

        :return: The is_custom of this Category.  # noqa: E501
        :rtype: bool
        """
        return self._is_custom

    @is_custom.setter
    def is_custom(self, is_custom):
        """Sets the is_custom of this Category.

        Whether the category is a finAPI global category (in which case this field will be false), or the category was created by a user (in which case this field will be true)  # noqa: E501

        :param is_custom: The is_custom of this Category.  # noqa: E501
        :type: bool
        """
        if is_custom is None:
            raise ValueError("Invalid value for `is_custom`, must not be `None`")  # noqa: E501

        self._is_custom = is_custom

    @property
    def children(self):
        """Gets the children of this Category.  # noqa: E501

        List of sub-categories identifiers (if any exist)  # noqa: E501

        :return: The children of this Category.  # noqa: E501
        :rtype: list[int]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this Category.

        List of sub-categories identifiers (if any exist)  # noqa: E501

        :param children: The children of this Category.  # noqa: E501
        :type: list[int]
        """

        self._children = children

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
        if not isinstance(other, Category):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
