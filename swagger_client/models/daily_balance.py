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


class DailyBalance(object):
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
        'date': 'str',
        'balance': 'float',
        'income': 'float',
        'spending': 'float',
        'transactions': 'list[int]'
    }

    attribute_map = {
        'date': 'date',
        'balance': 'balance',
        'income': 'income',
        'spending': 'spending',
        'transactions': 'transactions'
    }

    def __init__(self, date=None, balance=None, income=None, spending=None, transactions=None):  # noqa: E501
        """DailyBalance - a model defined in Swagger"""  # noqa: E501

        self._date = None
        self._balance = None
        self._income = None
        self._spending = None
        self._transactions = None
        self.discriminator = None

        self.date = date
        self.balance = balance
        self.income = income
        self.spending = spending
        self.transactions = transactions

    @property
    def date(self):
        """Gets the date of this DailyBalance.  # noqa: E501

        Date in the format 'yyyy-MM-dd HH:mm:ss.SSS' (german time).  # noqa: E501

        :return: The date of this DailyBalance.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this DailyBalance.

        Date in the format 'yyyy-MM-dd HH:mm:ss.SSS' (german time).  # noqa: E501

        :param date: The date of this DailyBalance.  # noqa: E501
        :type: str
        """
        if date is None:
            raise ValueError("Invalid value for `date`, must not be `None`")  # noqa: E501

        self._date = date

    @property
    def balance(self):
        """Gets the balance of this DailyBalance.  # noqa: E501

        Calculated account balance at the end of the given day.  # noqa: E501

        :return: The balance of this DailyBalance.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this DailyBalance.

        Calculated account balance at the end of the given day.  # noqa: E501

        :param balance: The balance of this DailyBalance.  # noqa: E501
        :type: float
        """
        if balance is None:
            raise ValueError("Invalid value for `balance`, must not be `None`")  # noqa: E501

        self._balance = balance

    @property
    def income(self):
        """Gets the income of this DailyBalance.  # noqa: E501

        The sum of income of the given day.  # noqa: E501

        :return: The income of this DailyBalance.  # noqa: E501
        :rtype: float
        """
        return self._income

    @income.setter
    def income(self, income):
        """Sets the income of this DailyBalance.

        The sum of income of the given day.  # noqa: E501

        :param income: The income of this DailyBalance.  # noqa: E501
        :type: float
        """
        if income is None:
            raise ValueError("Invalid value for `income`, must not be `None`")  # noqa: E501

        self._income = income

    @property
    def spending(self):
        """Gets the spending of this DailyBalance.  # noqa: E501

        The sum of spending of the given day.  # noqa: E501

        :return: The spending of this DailyBalance.  # noqa: E501
        :rtype: float
        """
        return self._spending

    @spending.setter
    def spending(self, spending):
        """Sets the spending of this DailyBalance.

        The sum of spending of the given day.  # noqa: E501

        :param spending: The spending of this DailyBalance.  # noqa: E501
        :type: float
        """
        if spending is None:
            raise ValueError("Invalid value for `spending`, must not be `None`")  # noqa: E501

        self._spending = spending

    @property
    def transactions(self):
        """Gets the transactions of this DailyBalance.  # noqa: E501

        Transactions for the given day  # noqa: E501

        :return: The transactions of this DailyBalance.  # noqa: E501
        :rtype: list[int]
        """
        return self._transactions

    @transactions.setter
    def transactions(self, transactions):
        """Sets the transactions of this DailyBalance.

        Transactions for the given day  # noqa: E501

        :param transactions: The transactions of this DailyBalance.  # noqa: E501
        :type: list[int]
        """
        if transactions is None:
            raise ValueError("Invalid value for `transactions`, must not be `None`")  # noqa: E501

        self._transactions = transactions

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
        if not isinstance(other, DailyBalance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
