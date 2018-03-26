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


class TransactionDataWithIdentifier(object):
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
        'account_type_id': 'int',
        'amount': 'float',
        'purpose': 'str',
        'counterpart': 'str',
        'counterpart_iban': 'str',
        'counterpart_account_number': 'str',
        'counterpart_blz': 'str',
        'counterpart_bic': 'str',
        'mc_code': 'str',
        'transaction_id': 'str'
    }

    attribute_map = {
        'account_type_id': 'accountTypeId',
        'amount': 'amount',
        'purpose': 'purpose',
        'counterpart': 'counterpart',
        'counterpart_iban': 'counterpartIban',
        'counterpart_account_number': 'counterpartAccountNumber',
        'counterpart_blz': 'counterpartBlz',
        'counterpart_bic': 'counterpartBic',
        'mc_code': 'mcCode',
        'transaction_id': 'transactionId'
    }

    def __init__(self, account_type_id=None, amount=None, purpose=None, counterpart=None, counterpart_iban=None, counterpart_account_number=None, counterpart_blz=None, counterpart_bic=None, mc_code=None, transaction_id=None):  # noqa: E501
        """TransactionDataWithIdentifier - a model defined in Swagger"""  # noqa: E501

        self._account_type_id = None
        self._amount = None
        self._purpose = None
        self._counterpart = None
        self._counterpart_iban = None
        self._counterpart_account_number = None
        self._counterpart_blz = None
        self._counterpart_bic = None
        self._mc_code = None
        self._transaction_id = None
        self.discriminator = None

        self.account_type_id = account_type_id
        self.amount = amount
        if purpose is not None:
            self.purpose = purpose
        if counterpart is not None:
            self.counterpart = counterpart
        if counterpart_iban is not None:
            self.counterpart_iban = counterpart_iban
        if counterpart_account_number is not None:
            self.counterpart_account_number = counterpart_account_number
        if counterpart_blz is not None:
            self.counterpart_blz = counterpart_blz
        if counterpart_bic is not None:
            self.counterpart_bic = counterpart_bic
        if mc_code is not None:
            self.mc_code = mc_code
        self.transaction_id = transaction_id

    @property
    def account_type_id(self):
        """Gets the account_type_id of this TransactionDataWithIdentifier.  # noqa: E501

        Identifier of account type.<br/><br/>1 = Checking,<br/>2 = Savings,<br/>3 = CreditCard,<br/>4 = Security,<br/>5 = Loan,<br/>6 = Pocket (DEPRECATED; will not be returned for any account unless this type has explicitly been set via PATCH),<br/>7 = Membership,<br/>8 = Bausparen<br/><br/>  # noqa: E501

        :return: The account_type_id of this TransactionDataWithIdentifier.  # noqa: E501
        :rtype: int
        """
        return self._account_type_id

    @account_type_id.setter
    def account_type_id(self, account_type_id):
        """Sets the account_type_id of this TransactionDataWithIdentifier.

        Identifier of account type.<br/><br/>1 = Checking,<br/>2 = Savings,<br/>3 = CreditCard,<br/>4 = Security,<br/>5 = Loan,<br/>6 = Pocket (DEPRECATED; will not be returned for any account unless this type has explicitly been set via PATCH),<br/>7 = Membership,<br/>8 = Bausparen<br/><br/>  # noqa: E501

        :param account_type_id: The account_type_id of this TransactionDataWithIdentifier.  # noqa: E501
        :type: int
        """
        if account_type_id is None:
            raise ValueError("Invalid value for `account_type_id`, must not be `None`")  # noqa: E501
        if account_type_id is not None and account_type_id > 7:  # noqa: E501
            raise ValueError("Invalid value for `account_type_id`, must be a value less than or equal to `7`")  # noqa: E501
        if account_type_id is not None and account_type_id < 1:  # noqa: E501
            raise ValueError("Invalid value for `account_type_id`, must be a value greater than or equal to `1`")  # noqa: E501

        self._account_type_id = account_type_id

    @property
    def amount(self):
        """Gets the amount of this TransactionDataWithIdentifier.  # noqa: E501

        Amount  # noqa: E501

        :return: The amount of this TransactionDataWithIdentifier.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TransactionDataWithIdentifier.

        Amount  # noqa: E501

        :param amount: The amount of this TransactionDataWithIdentifier.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def purpose(self):
        """Gets the purpose of this TransactionDataWithIdentifier.  # noqa: E501

        Purpose. Any symbols are allowed. Maximum length is 2000. Default value: null.  # noqa: E501

        :return: The purpose of this TransactionDataWithIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        """Sets the purpose of this TransactionDataWithIdentifier.

        Purpose. Any symbols are allowed. Maximum length is 2000. Default value: null.  # noqa: E501

        :param purpose: The purpose of this TransactionDataWithIdentifier.  # noqa: E501
        :type: str
        """

        self._purpose = purpose

    @property
    def counterpart(self):
        """Gets the counterpart of this TransactionDataWithIdentifier.  # noqa: E501

        Counterpart. Any symbols are allowed. Maximum length is 80. Default value: null.  # noqa: E501

        :return: The counterpart of this TransactionDataWithIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._counterpart

    @counterpart.setter
    def counterpart(self, counterpart):
        """Sets the counterpart of this TransactionDataWithIdentifier.

        Counterpart. Any symbols are allowed. Maximum length is 80. Default value: null.  # noqa: E501

        :param counterpart: The counterpart of this TransactionDataWithIdentifier.  # noqa: E501
        :type: str
        """

        self._counterpart = counterpart

    @property
    def counterpart_iban(self):
        """Gets the counterpart_iban of this TransactionDataWithIdentifier.  # noqa: E501

        Counterpart IBAN. Default value: null.  # noqa: E501

        :return: The counterpart_iban of this TransactionDataWithIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._counterpart_iban

    @counterpart_iban.setter
    def counterpart_iban(self, counterpart_iban):
        """Sets the counterpart_iban of this TransactionDataWithIdentifier.

        Counterpart IBAN. Default value: null.  # noqa: E501

        :param counterpart_iban: The counterpart_iban of this TransactionDataWithIdentifier.  # noqa: E501
        :type: str
        """

        self._counterpart_iban = counterpart_iban

    @property
    def counterpart_account_number(self):
        """Gets the counterpart_account_number of this TransactionDataWithIdentifier.  # noqa: E501

        Counterpart account number. Default value: null.  # noqa: E501

        :return: The counterpart_account_number of this TransactionDataWithIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._counterpart_account_number

    @counterpart_account_number.setter
    def counterpart_account_number(self, counterpart_account_number):
        """Sets the counterpart_account_number of this TransactionDataWithIdentifier.

        Counterpart account number. Default value: null.  # noqa: E501

        :param counterpart_account_number: The counterpart_account_number of this TransactionDataWithIdentifier.  # noqa: E501
        :type: str
        """

        self._counterpart_account_number = counterpart_account_number

    @property
    def counterpart_blz(self):
        """Gets the counterpart_blz of this TransactionDataWithIdentifier.  # noqa: E501

        Counterpart BLZ. Default value: null.  # noqa: E501

        :return: The counterpart_blz of this TransactionDataWithIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._counterpart_blz

    @counterpart_blz.setter
    def counterpart_blz(self, counterpart_blz):
        """Sets the counterpart_blz of this TransactionDataWithIdentifier.

        Counterpart BLZ. Default value: null.  # noqa: E501

        :param counterpart_blz: The counterpart_blz of this TransactionDataWithIdentifier.  # noqa: E501
        :type: str
        """

        self._counterpart_blz = counterpart_blz

    @property
    def counterpart_bic(self):
        """Gets the counterpart_bic of this TransactionDataWithIdentifier.  # noqa: E501

        Counterpart BIC. Default value: null.  # noqa: E501

        :return: The counterpart_bic of this TransactionDataWithIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._counterpart_bic

    @counterpart_bic.setter
    def counterpart_bic(self, counterpart_bic):
        """Sets the counterpart_bic of this TransactionDataWithIdentifier.

        Counterpart BIC. Default value: null.  # noqa: E501

        :param counterpart_bic: The counterpart_bic of this TransactionDataWithIdentifier.  # noqa: E501
        :type: str
        """

        self._counterpart_bic = counterpart_bic

    @property
    def mc_code(self):
        """Gets the mc_code of this TransactionDataWithIdentifier.  # noqa: E501

        Merchant category code (for credit card transactions only). Default value: null. NOTE: This field is currently not regarded.  # noqa: E501

        :return: The mc_code of this TransactionDataWithIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._mc_code

    @mc_code.setter
    def mc_code(self, mc_code):
        """Sets the mc_code of this TransactionDataWithIdentifier.

        Merchant category code (for credit card transactions only). Default value: null. NOTE: This field is currently not regarded.  # noqa: E501

        :param mc_code: The mc_code of this TransactionDataWithIdentifier.  # noqa: E501
        :type: str
        """

        self._mc_code = mc_code

    @property
    def transaction_id(self):
        """Gets the transaction_id of this TransactionDataWithIdentifier.  # noqa: E501

        Identifier of transaction. This can be any arbitrary string that will be passed back in the response so that you can map the results to the given transactions. Note that the identifier must be unique within the given list of transactions.  # noqa: E501

        :return: The transaction_id of this TransactionDataWithIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this TransactionDataWithIdentifier.

        Identifier of transaction. This can be any arbitrary string that will be passed back in the response so that you can map the results to the given transactions. Note that the identifier must be unique within the given list of transactions.  # noqa: E501

        :param transaction_id: The transaction_id of this TransactionDataWithIdentifier.  # noqa: E501
        :type: str
        """
        if transaction_id is None:
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")  # noqa: E501

        self._transaction_id = transaction_id

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
        if not isinstance(other, TransactionDataWithIdentifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
