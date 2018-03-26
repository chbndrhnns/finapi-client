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


class SingleMoneyTransferRecipientData(object):
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
        'recipient_name': 'str',
        'recipient_iban': 'str',
        'recipient_bic': 'str',
        'clearing_account_id': 'str',
        'amount': 'float',
        'purpose': 'str'
    }

    attribute_map = {
        'recipient_name': 'recipientName',
        'recipient_iban': 'recipientIban',
        'recipient_bic': 'recipientBic',
        'clearing_account_id': 'clearingAccountId',
        'amount': 'amount',
        'purpose': 'purpose'
    }

    def __init__(self, recipient_name=None, recipient_iban=None, recipient_bic=None, clearing_account_id=None, amount=None, purpose=None):  # noqa: E501
        """SingleMoneyTransferRecipientData - a model defined in Swagger"""  # noqa: E501

        self._recipient_name = None
        self._recipient_iban = None
        self._recipient_bic = None
        self._clearing_account_id = None
        self._amount = None
        self._purpose = None
        self.discriminator = None

        if recipient_name is not None:
            self.recipient_name = recipient_name
        if recipient_iban is not None:
            self.recipient_iban = recipient_iban
        if recipient_bic is not None:
            self.recipient_bic = recipient_bic
        if clearing_account_id is not None:
            self.clearing_account_id = clearing_account_id
        self.amount = amount
        if purpose is not None:
            self.purpose = purpose

    @property
    def recipient_name(self):
        """Gets the recipient_name of this SingleMoneyTransferRecipientData.  # noqa: E501

        Name of the recipient. Note: Neither finAPI nor the involved bank servers are guaranteed to validate the recipient name. Even if the recipient name does not depict the actual registered account holder of the specified recipient account, the money transfer request might still be successful. This field is optional only when you pass a clearing account as the recipient. Otherwise, this field is required.  # noqa: E501

        :return: The recipient_name of this SingleMoneyTransferRecipientData.  # noqa: E501
        :rtype: str
        """
        return self._recipient_name

    @recipient_name.setter
    def recipient_name(self, recipient_name):
        """Sets the recipient_name of this SingleMoneyTransferRecipientData.

        Name of the recipient. Note: Neither finAPI nor the involved bank servers are guaranteed to validate the recipient name. Even if the recipient name does not depict the actual registered account holder of the specified recipient account, the money transfer request might still be successful. This field is optional only when you pass a clearing account as the recipient. Otherwise, this field is required.  # noqa: E501

        :param recipient_name: The recipient_name of this SingleMoneyTransferRecipientData.  # noqa: E501
        :type: str
        """

        self._recipient_name = recipient_name

    @property
    def recipient_iban(self):
        """Gets the recipient_iban of this SingleMoneyTransferRecipientData.  # noqa: E501

        IBAN of the recipient's account. This field is optional only when you pass a clearing account as the recipient. Otherwise, this field is required.  # noqa: E501

        :return: The recipient_iban of this SingleMoneyTransferRecipientData.  # noqa: E501
        :rtype: str
        """
        return self._recipient_iban

    @recipient_iban.setter
    def recipient_iban(self, recipient_iban):
        """Sets the recipient_iban of this SingleMoneyTransferRecipientData.

        IBAN of the recipient's account. This field is optional only when you pass a clearing account as the recipient. Otherwise, this field is required.  # noqa: E501

        :param recipient_iban: The recipient_iban of this SingleMoneyTransferRecipientData.  # noqa: E501
        :type: str
        """

        self._recipient_iban = recipient_iban

    @property
    def recipient_bic(self):
        """Gets the recipient_bic of this SingleMoneyTransferRecipientData.  # noqa: E501

        BIC of the recipient's account. Note: This field is optional when you pass a clearing account as the recipient or if the bank connection of the account that you want to transfer money from supports the IBAN-Only money transfer. You can find this out via GET /bankConnections/<id>. Also note that when a BIC is given, then this BIC will be used for the money transfer request independent of whether it is required or not (unless you pass a clearing account, in which case this field will always be ignored).  # noqa: E501

        :return: The recipient_bic of this SingleMoneyTransferRecipientData.  # noqa: E501
        :rtype: str
        """
        return self._recipient_bic

    @recipient_bic.setter
    def recipient_bic(self, recipient_bic):
        """Sets the recipient_bic of this SingleMoneyTransferRecipientData.

        BIC of the recipient's account. Note: This field is optional when you pass a clearing account as the recipient or if the bank connection of the account that you want to transfer money from supports the IBAN-Only money transfer. You can find this out via GET /bankConnections/<id>. Also note that when a BIC is given, then this BIC will be used for the money transfer request independent of whether it is required or not (unless you pass a clearing account, in which case this field will always be ignored).  # noqa: E501

        :param recipient_bic: The recipient_bic of this SingleMoneyTransferRecipientData.  # noqa: E501
        :type: str
        """

        self._recipient_bic = recipient_bic

    @property
    def clearing_account_id(self):
        """Gets the clearing_account_id of this SingleMoneyTransferRecipientData.  # noqa: E501

        Identifier of a clearing account. If this field is set, then the fields 'recipientName', 'recipientIban' and 'recipientBic' will be ignored and the recipient account will be the specified clearing account.  # noqa: E501

        :return: The clearing_account_id of this SingleMoneyTransferRecipientData.  # noqa: E501
        :rtype: str
        """
        return self._clearing_account_id

    @clearing_account_id.setter
    def clearing_account_id(self, clearing_account_id):
        """Sets the clearing_account_id of this SingleMoneyTransferRecipientData.

        Identifier of a clearing account. If this field is set, then the fields 'recipientName', 'recipientIban' and 'recipientBic' will be ignored and the recipient account will be the specified clearing account.  # noqa: E501

        :param clearing_account_id: The clearing_account_id of this SingleMoneyTransferRecipientData.  # noqa: E501
        :type: str
        """

        self._clearing_account_id = clearing_account_id

    @property
    def amount(self):
        """Gets the amount of this SingleMoneyTransferRecipientData.  # noqa: E501

        The amount to transfer. Must be a positive decimal number with at most two decimal places (e.g. 99.90)  # noqa: E501

        :return: The amount of this SingleMoneyTransferRecipientData.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this SingleMoneyTransferRecipientData.

        The amount to transfer. Must be a positive decimal number with at most two decimal places (e.g. 99.90)  # noqa: E501

        :param amount: The amount of this SingleMoneyTransferRecipientData.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def purpose(self):
        """Gets the purpose of this SingleMoneyTransferRecipientData.  # noqa: E501

        The purpose of the transfer transaction  # noqa: E501

        :return: The purpose of this SingleMoneyTransferRecipientData.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this SingleMoneyTransferRecipientData.

        The purpose of the transfer transaction  # noqa: E501

        :param purpose: The purpose of this SingleMoneyTransferRecipientData.  # noqa: E501
        :type: str
        """

        self._purpose = purpose

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
        if not isinstance(other, SingleMoneyTransferRecipientData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
