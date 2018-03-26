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


class Security(object):
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
        'account_id': 'int',
        'name': 'str',
        'isin': 'str',
        'wkn': 'str',
        'quote': 'float',
        'quote_currency': 'str',
        'quote_type': 'str',
        'quote_date': 'str',
        'quantity_nominal': 'float',
        'quantity_nominal_type': 'str',
        'market_value': 'float',
        'market_value_currency': 'str',
        'entry_quote': 'float',
        'entry_quote_currency': 'str'
    }

    attribute_map = {
        'id': 'id',
        'account_id': 'accountId',
        'name': 'name',
        'isin': 'isin',
        'wkn': 'wkn',
        'quote': 'quote',
        'quote_currency': 'quoteCurrency',
        'quote_type': 'quoteType',
        'quote_date': 'quoteDate',
        'quantity_nominal': 'quantityNominal',
        'quantity_nominal_type': 'quantityNominalType',
        'market_value': 'marketValue',
        'market_value_currency': 'marketValueCurrency',
        'entry_quote': 'entryQuote',
        'entry_quote_currency': 'entryQuoteCurrency'
    }

    def __init__(self, id=None, account_id=None, name=None, isin=None, wkn=None, quote=None, quote_currency=None, quote_type=None, quote_date=None, quantity_nominal=None, quantity_nominal_type=None, market_value=None, market_value_currency=None, entry_quote=None, entry_quote_currency=None):  # noqa: E501
        """Security - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._account_id = None
        self._name = None
        self._isin = None
        self._wkn = None
        self._quote = None
        self._quote_currency = None
        self._quote_type = None
        self._quote_date = None
        self._quantity_nominal = None
        self._quantity_nominal_type = None
        self._market_value = None
        self._market_value_currency = None
        self._entry_quote = None
        self._entry_quote_currency = None
        self.discriminator = None

        self.id = id
        self.account_id = account_id
        if name is not None:
            self.name = name
        if isin is not None:
            self.isin = isin
        if wkn is not None:
            self.wkn = wkn
        if quote is not None:
            self.quote = quote
        if quote_currency is not None:
            self.quote_currency = quote_currency
        if quote_type is not None:
            self.quote_type = quote_type
        if quote_date is not None:
            self.quote_date = quote_date
        if quantity_nominal is not None:
            self.quantity_nominal = quantity_nominal
        if quantity_nominal_type is not None:
            self.quantity_nominal_type = quantity_nominal_type
        if market_value is not None:
            self.market_value = market_value
        if market_value_currency is not None:
            self.market_value_currency = market_value_currency
        if entry_quote is not None:
            self.entry_quote = entry_quote
        if entry_quote_currency is not None:
            self.entry_quote_currency = entry_quote_currency

    @property
    def id(self):
        """Gets the id of this Security.  # noqa: E501

        Identifier. Note: Whenever a security account is being updated, its security positions will be internally re-created, meaning that the identifier of a security position might change over time.  # noqa: E501

        :return: The id of this Security.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Security.

        Identifier. Note: Whenever a security account is being updated, its security positions will be internally re-created, meaning that the identifier of a security position might change over time.  # noqa: E501

        :param id: The id of this Security.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def account_id(self):
        """Gets the account_id of this Security.  # noqa: E501

        Security account identifier  # noqa: E501

        :return: The account_id of this Security.  # noqa: E501
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Security.

        Security account identifier  # noqa: E501

        :param account_id: The account_id of this Security.  # noqa: E501
        :type: int
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def name(self):
        """Gets the name of this Security.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this Security.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Security.

        Name  # noqa: E501

        :param name: The name of this Security.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def isin(self):
        """Gets the isin of this Security.  # noqa: E501

        ISIN  # noqa: E501

        :return: The isin of this Security.  # noqa: E501
        :rtype: str
        """
        return self._isin

    @isin.setter
    def isin(self, isin):
        """Sets the isin of this Security.

        ISIN  # noqa: E501

        :param isin: The isin of this Security.  # noqa: E501
        :type: str
        """

        self._isin = isin

    @property
    def wkn(self):
        """Gets the wkn of this Security.  # noqa: E501

        WKN  # noqa: E501

        :return: The wkn of this Security.  # noqa: E501
        :rtype: str
        """
        return self._wkn

    @wkn.setter
    def wkn(self, wkn):
        """Sets the wkn of this Security.

        WKN  # noqa: E501

        :param wkn: The wkn of this Security.  # noqa: E501
        :type: str
        """

        self._wkn = wkn

    @property
    def quote(self):
        """Gets the quote of this Security.  # noqa: E501

        Quote  # noqa: E501

        :return: The quote of this Security.  # noqa: E501
        :rtype: float
        """
        return self._quote

    @quote.setter
    def quote(self, quote):
        """Sets the quote of this Security.

        Quote  # noqa: E501

        :param quote: The quote of this Security.  # noqa: E501
        :type: float
        """

        self._quote = quote

    @property
    def quote_currency(self):
        """Gets the quote_currency of this Security.  # noqa: E501

        Currency of quote  # noqa: E501

        :return: The quote_currency of this Security.  # noqa: E501
        :rtype: str
        """
        return self._quote_currency

    @quote_currency.setter
    def quote_currency(self, quote_currency):
        """Sets the quote_currency of this Security.

        Currency of quote  # noqa: E501

        :param quote_currency: The quote_currency of this Security.  # noqa: E501
        :type: str
        """

        self._quote_currency = quote_currency

    @property
    def quote_type(self):
        """Gets the quote_type of this Security.  # noqa: E501

        Type of quote. 'PERC' if quote is a percentage value, 'ACTU' if quote is the actual amount  # noqa: E501

        :return: The quote_type of this Security.  # noqa: E501
        :rtype: str
        """
        return self._quote_type

    @quote_type.setter
    def quote_type(self, quote_type):
        """Sets the quote_type of this Security.

        Type of quote. 'PERC' if quote is a percentage value, 'ACTU' if quote is the actual amount  # noqa: E501

        :param quote_type: The quote_type of this Security.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTU", "PERC"]  # noqa: E501
        if quote_type not in allowed_values:
            raise ValueError(
                "Invalid value for `quote_type` ({0}), must be one of {1}"  # noqa: E501
                .format(quote_type, allowed_values)
            )

        self._quote_type = quote_type

    @property
    def quote_date(self):
        """Gets the quote_date of this Security.  # noqa: E501

        Quote date  # noqa: E501

        :return: The quote_date of this Security.  # noqa: E501
        :rtype: str
        """
        return self._quote_date

    @quote_date.setter
    def quote_date(self, quote_date):
        """Sets the quote_date of this Security.

        Quote date  # noqa: E501

        :param quote_date: The quote_date of this Security.  # noqa: E501
        :type: str
        """

        self._quote_date = quote_date

    @property
    def quantity_nominal(self):
        """Gets the quantity_nominal of this Security.  # noqa: E501

        Value of quantity or nominal  # noqa: E501

        :return: The quantity_nominal of this Security.  # noqa: E501
        :rtype: float
        """
        return self._quantity_nominal

    @quantity_nominal.setter
    def quantity_nominal(self, quantity_nominal):
        """Sets the quantity_nominal of this Security.

        Value of quantity or nominal  # noqa: E501

        :param quantity_nominal: The quantity_nominal of this Security.  # noqa: E501
        :type: float
        """

        self._quantity_nominal = quantity_nominal

    @property
    def quantity_nominal_type(self):
        """Gets the quantity_nominal_type of this Security.  # noqa: E501

        Type of quantity or nominal value. 'UNIT' if value is a quantity, 'FAMT' if value is the nominal amount  # noqa: E501

        :return: The quantity_nominal_type of this Security.  # noqa: E501
        :rtype: str
        """
        return self._quantity_nominal_type

    @quantity_nominal_type.setter
    def quantity_nominal_type(self, quantity_nominal_type):
        """Sets the quantity_nominal_type of this Security.

        Type of quantity or nominal value. 'UNIT' if value is a quantity, 'FAMT' if value is the nominal amount  # noqa: E501

        :param quantity_nominal_type: The quantity_nominal_type of this Security.  # noqa: E501
        :type: str
        """
        allowed_values = ["UNIT", "FAMT"]  # noqa: E501
        if quantity_nominal_type not in allowed_values:
            raise ValueError(
                "Invalid value for `quantity_nominal_type` ({0}), must be one of {1}"  # noqa: E501
                .format(quantity_nominal_type, allowed_values)
            )

        self._quantity_nominal_type = quantity_nominal_type

    @property
    def market_value(self):
        """Gets the market_value of this Security.  # noqa: E501

        Market value  # noqa: E501

        :return: The market_value of this Security.  # noqa: E501
        :rtype: float
        """
        return self._market_value

    @market_value.setter
    def market_value(self, market_value):
        """Sets the market_value of this Security.

        Market value  # noqa: E501

        :param market_value: The market_value of this Security.  # noqa: E501
        :type: float
        """

        self._market_value = market_value

    @property
    def market_value_currency(self):
        """Gets the market_value_currency of this Security.  # noqa: E501

        Currency of market value  # noqa: E501

        :return: The market_value_currency of this Security.  # noqa: E501
        :rtype: str
        """
        return self._market_value_currency

    @market_value_currency.setter
    def market_value_currency(self, market_value_currency):
        """Sets the market_value_currency of this Security.

        Currency of market value  # noqa: E501

        :param market_value_currency: The market_value_currency of this Security.  # noqa: E501
        :type: str
        """

        self._market_value_currency = market_value_currency

    @property
    def entry_quote(self):
        """Gets the entry_quote of this Security.  # noqa: E501

        Entry quote  # noqa: E501

        :return: The entry_quote of this Security.  # noqa: E501
        :rtype: float
        """
        return self._entry_quote

    @entry_quote.setter
    def entry_quote(self, entry_quote):
        """Sets the entry_quote of this Security.

        Entry quote  # noqa: E501

        :param entry_quote: The entry_quote of this Security.  # noqa: E501
        :type: float
        """

        self._entry_quote = entry_quote

    @property
    def entry_quote_currency(self):
        """Gets the entry_quote_currency of this Security.  # noqa: E501

        Currency of entry quote  # noqa: E501

        :return: The entry_quote_currency of this Security.  # noqa: E501
        :rtype: str
        """
        return self._entry_quote_currency

    @entry_quote_currency.setter
    def entry_quote_currency(self, entry_quote_currency):
        """Sets the entry_quote_currency of this Security.

        Currency of entry quote  # noqa: E501

        :param entry_quote_currency: The entry_quote_currency of this Security.  # noqa: E501
        :type: str
        """

        self._entry_quote_currency = entry_quote_currency

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
        if not isinstance(other, Security):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
