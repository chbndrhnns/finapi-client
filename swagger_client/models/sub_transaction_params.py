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


class SubTransactionParams(object):
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
        'amount': 'float',
        'category_id': 'int',
        'purpose': 'str',
        'counterpart': 'str',
        'counterpart_account_number': 'str',
        'counterpart_iban': 'str',
        'counterpart_bic': 'str',
        'counterpart_blz': 'str',
        'label_ids': 'list[int]'
    }

    attribute_map = {
        'amount': 'amount',
        'category_id': 'categoryId',
        'purpose': 'purpose',
        'counterpart': 'counterpart',
        'counterpart_account_number': 'counterpartAccountNumber',
        'counterpart_iban': 'counterpartIban',
        'counterpart_bic': 'counterpartBic',
        'counterpart_blz': 'counterpartBlz',
        'label_ids': 'labelIds'
    }

    def __init__(self, amount=None, category_id=None, purpose=None, counterpart=None, counterpart_account_number=None, counterpart_iban=None, counterpart_bic=None, counterpart_blz=None, label_ids=None):  # noqa: E501
        """SubTransactionParams - a model defined in Swagger"""  # noqa: E501

        self._amount = None
        self._category_id = None
        self._purpose = None
        self._counterpart = None
        self._counterpart_account_number = None
        self._counterpart_iban = None
        self._counterpart_bic = None
        self._counterpart_blz = None
        self._label_ids = None
        self.discriminator = None

        self.amount = amount
        if category_id is not None:
            self.category_id = category_id
        if purpose is not None:
            self.purpose = purpose
        if counterpart is not None:
            self.counterpart = counterpart
        if counterpart_account_number is not None:
            self.counterpart_account_number = counterpart_account_number
        if counterpart_iban is not None:
            self.counterpart_iban = counterpart_iban
        if counterpart_bic is not None:
            self.counterpart_bic = counterpart_bic
        if counterpart_blz is not None:
            self.counterpart_blz = counterpart_blz
        if label_ids is not None:
            self.label_ids = label_ids

    @property
    def amount(self):
        """Gets the amount of this SubTransactionParams.  # noqa: E501

        Amount  # noqa: E501

        :return: The amount of this SubTransactionParams.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SubTransactionParams.

        Amount  # noqa: E501

        :param amount: The amount of this SubTransactionParams.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def category_id(self):
        """Gets the category_id of this SubTransactionParams.  # noqa: E501

        Category identifier. If not specified, the original transaction's category will be applied. If you explicitly want the sub-transaction to have no category, then pass this field with value '0' (zero).  # noqa: E501

        :return: The category_id of this SubTransactionParams.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this SubTransactionParams.

        Category identifier. If not specified, the original transaction's category will be applied. If you explicitly want the sub-transaction to have no category, then pass this field with value '0' (zero).  # noqa: E501

        :param category_id: The category_id of this SubTransactionParams.  # noqa: E501
        :type: int
        """

        self._category_id = category_id

    @property
    def purpose(self):
        """Gets the purpose of this SubTransactionParams.  # noqa: E501

        Purpose. Maximum length is 2000. If not specified, the original transaction's value will be applied.  # noqa: E501

        :return: The purpose of this SubTransactionParams.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this SubTransactionParams.

        Purpose. Maximum length is 2000. If not specified, the original transaction's value will be applied.  # noqa: E501

        :param purpose: The purpose of this SubTransactionParams.  # noqa: E501
        :type: str
        """
        if purpose is not None and not re.search('[A-Za-z0-9¡-ʯ &\\(\\)\\{\\}\\[\\]\\.:,;\\?!\\+\\-_\\$@#~`\\^€]*', purpose):  # noqa: E501
            raise ValueError("Invalid value for `purpose`, must be a follow pattern or equal to `/[A-Za-z0-9¡-ʯ &\\(\\)\\{\\}\\[\\]\\.:,;\\?!\\+\\-_\\$@#~`\\^€]*/`")  # noqa: E501

        self._purpose = purpose

    @property
    def counterpart(self):
        """Gets the counterpart of this SubTransactionParams.  # noqa: E501

        Counterpart. Maximum length is 80. If not specified, the original transaction's value will be applied.  # noqa: E501

        :return: The counterpart of this SubTransactionParams.  # noqa: E501
        :rtype: str
        """
        return self._counterpart

    @counterpart.setter
    def counterpart(self, counterpart):
        """Sets the counterpart of this SubTransactionParams.

        Counterpart. Maximum length is 80. If not specified, the original transaction's value will be applied.  # noqa: E501

        :param counterpart: The counterpart of this SubTransactionParams.  # noqa: E501
        :type: str
        """
        if counterpart is not None and not re.search('[A-Za-z0-9¡-ʯ &\\(\\)\\{\\}\\[\\]\\.:,;\\?!\\+\\-_\\$@#~`\\^€]*', counterpart):  # noqa: E501
            raise ValueError("Invalid value for `counterpart`, must be a follow pattern or equal to `/[A-Za-z0-9¡-ʯ &\\(\\)\\{\\}\\[\\]\\.:,;\\?!\\+\\-_\\$@#~`\\^€]*/`")  # noqa: E501

        self._counterpart = counterpart

    @property
    def counterpart_account_number(self):
        """Gets the counterpart_account_number of this SubTransactionParams.  # noqa: E501

        Counterpart account number. If not specified, the original transaction's value will be applied.  # noqa: E501

        :return: The counterpart_account_number of this SubTransactionParams.  # noqa: E501
        :rtype: str
        """
        return self._counterpart_account_number

    @counterpart_account_number.setter
    def counterpart_account_number(self, counterpart_account_number):
        """Sets the counterpart_account_number of this SubTransactionParams.

        Counterpart account number. If not specified, the original transaction's value will be applied.  # noqa: E501

        :param counterpart_account_number: The counterpart_account_number of this SubTransactionParams.  # noqa: E501
        :type: str
        """
        if counterpart_account_number is not None and not re.search('[A-Za-z0-9¡-ʯ &\\(\\)\\{\\}\\[\\]\\.:,;\\?!\\+\\-_\\$@#~`\\^€]*', counterpart_account_number):  # noqa: E501
            raise ValueError("Invalid value for `counterpart_account_number`, must be a follow pattern or equal to `/[A-Za-z0-9¡-ʯ &\\(\\)\\{\\}\\[\\]\\.:,;\\?!\\+\\-_\\$@#~`\\^€]*/`")  # noqa: E501

        self._counterpart_account_number = counterpart_account_number

    @property
    def counterpart_iban(self):
        """Gets the counterpart_iban of this SubTransactionParams.  # noqa: E501

        Counterpart IBAN. If not specified, the original transaction's value will be applied.  # noqa: E501

        :return: The counterpart_iban of this SubTransactionParams.  # noqa: E501
        :rtype: str
        """
        return self._counterpart_iban

    @counterpart_iban.setter
    def counterpart_iban(self, counterpart_iban):
        """Sets the counterpart_iban of this SubTransactionParams.

        Counterpart IBAN. If not specified, the original transaction's value will be applied.  # noqa: E501

        :param counterpart_iban: The counterpart_iban of this SubTransactionParams.  # noqa: E501
        :type: str
        """

        self._counterpart_iban = counterpart_iban

    @property
    def counterpart_bic(self):
        """Gets the counterpart_bic of this SubTransactionParams.  # noqa: E501

        Counterpart BIC. If not specified, the original transaction's value will be applied.  # noqa: E501

        :return: The counterpart_bic of this SubTransactionParams.  # noqa: E501
        :rtype: str
        """
        return self._counterpart_bic

    @counterpart_bic.setter
    def counterpart_bic(self, counterpart_bic):
        """Sets the counterpart_bic of this SubTransactionParams.

        Counterpart BIC. If not specified, the original transaction's value will be applied.  # noqa: E501

        :param counterpart_bic: The counterpart_bic of this SubTransactionParams.  # noqa: E501
        :type: str
        """

        self._counterpart_bic = counterpart_bic

    @property
    def counterpart_blz(self):
        """Gets the counterpart_blz of this SubTransactionParams.  # noqa: E501

        Counterpart BLZ. If not specified, the original transaction's value will be applied.  # noqa: E501

        :return: The counterpart_blz of this SubTransactionParams.  # noqa: E501
        :rtype: str
        """
        return self._counterpart_blz

    @counterpart_blz.setter
    def counterpart_blz(self, counterpart_blz):
        """Sets the counterpart_blz of this SubTransactionParams.

        Counterpart BLZ. If not specified, the original transaction's value will be applied.  # noqa: E501

        :param counterpart_blz: The counterpart_blz of this SubTransactionParams.  # noqa: E501
        :type: str
        """

        self._counterpart_blz = counterpart_blz

    @property
    def label_ids(self):
        """Gets the label_ids of this SubTransactionParams.  # noqa: E501

        List of connected labels. Note that when this field is not specified, then the labels of the original transaction will NOT get applied to the sub-transaction. Instead, the sub-transaction will have no labels assigned to it.  # noqa: E501

        :return: The label_ids of this SubTransactionParams.  # noqa: E501
        :rtype: list[int]
        """
        return self._label_ids

    @label_ids.setter
    def label_ids(self, label_ids):
        """Sets the label_ids of this SubTransactionParams.

        List of connected labels. Note that when this field is not specified, then the labels of the original transaction will NOT get applied to the sub-transaction. Instead, the sub-transaction will have no labels assigned to it.  # noqa: E501

        :param label_ids: The label_ids of this SubTransactionParams.  # noqa: E501
        :type: list[int]
        """

        self._label_ids = label_ids

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
        if not isinstance(other, SubTransactionParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
