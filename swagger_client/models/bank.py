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


class Bank(object):
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
        'login_hint': 'str',
        'bic': 'str',
        'blz': 'str',
        'blzs': 'list[str]',
        'login_field_user_id': 'str',
        'login_field_customer_id': 'str',
        'login_field_pin': 'str',
        'is_supported': 'bool',
        'supported_data_sources': 'list[str]',
        'pins_are_volatile': 'bool',
        'location': 'str',
        'city': 'str',
        'is_test_bank': 'bool',
        'popularity': 'int',
        'health': 'int',
        'last_communication_attempt': 'str',
        'last_successful_communication': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'login_hint': 'loginHint',
        'bic': 'bic',
        'blz': 'blz',
        'blzs': 'blzs',
        'login_field_user_id': 'loginFieldUserId',
        'login_field_customer_id': 'loginFieldCustomerId',
        'login_field_pin': 'loginFieldPin',
        'is_supported': 'isSupported',
        'supported_data_sources': 'supportedDataSources',
        'pins_are_volatile': 'pinsAreVolatile',
        'location': 'location',
        'city': 'city',
        'is_test_bank': 'isTestBank',
        'popularity': 'popularity',
        'health': 'health',
        'last_communication_attempt': 'lastCommunicationAttempt',
        'last_successful_communication': 'lastSuccessfulCommunication'
    }

    def __init__(self, id=None, name=None, login_hint=None, bic=None, blz=None, blzs=None, login_field_user_id=None, login_field_customer_id=None, login_field_pin=None, is_supported=False, supported_data_sources=None, pins_are_volatile=False, location=None, city=None, is_test_bank=False, popularity=None, health=None, last_communication_attempt=None, last_successful_communication=None):  # noqa: E501
        """Bank - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._login_hint = None
        self._bic = None
        self._blz = None
        self._blzs = None
        self._login_field_user_id = None
        self._login_field_customer_id = None
        self._login_field_pin = None
        self._is_supported = None
        self._supported_data_sources = None
        self._pins_are_volatile = None
        self._location = None
        self._city = None
        self._is_test_bank = None
        self._popularity = None
        self._health = None
        self._last_communication_attempt = None
        self._last_successful_communication = None
        self.discriminator = None

        self.id = id
        self.name = name
        if login_hint is not None:
            self.login_hint = login_hint
        if bic is not None:
            self.bic = bic
        self.blz = blz
        self.blzs = blzs
        if login_field_user_id is not None:
            self.login_field_user_id = login_field_user_id
        if login_field_customer_id is not None:
            self.login_field_customer_id = login_field_customer_id
        if login_field_pin is not None:
            self.login_field_pin = login_field_pin
        self.is_supported = is_supported
        self.supported_data_sources = supported_data_sources
        self.pins_are_volatile = pins_are_volatile
        if location is not None:
            self.location = location
        if city is not None:
            self.city = city
        self.is_test_bank = is_test_bank
        self.popularity = popularity
        self.health = health
        if last_communication_attempt is not None:
            self.last_communication_attempt = last_communication_attempt
        if last_successful_communication is not None:
            self.last_successful_communication = last_successful_communication

    @property
    def id(self):
        """Gets the id of this Bank.  # noqa: E501

        Bank identifier.<br/><br/>NOTE: Do NOT assume that the identifiers of banks are the same across different finAPI environments. In fact, the identifiers may change whenever a new finAPI version is released, even within the same environment. The identifiers are meant to be used for references within the finAPI services only, but not for hard-coding them in your application. If you need to hard-code the usage of a certain bank within your application, please instead refer to the BLZ.  # noqa: E501

        :return: The id of this Bank.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Bank.

        Bank identifier.<br/><br/>NOTE: Do NOT assume that the identifiers of banks are the same across different finAPI environments. In fact, the identifiers may change whenever a new finAPI version is released, even within the same environment. The identifiers are meant to be used for references within the finAPI services only, but not for hard-coding them in your application. If you need to hard-code the usage of a certain bank within your application, please instead refer to the BLZ.  # noqa: E501

        :param id: The id of this Bank.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Bank.  # noqa: E501

        Name of bank  # noqa: E501

        :return: The name of this Bank.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Bank.

        Name of bank  # noqa: E501

        :param name: The name of this Bank.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def login_hint(self):
        """Gets the login_hint of this Bank.  # noqa: E501

        Login hint. Contains a German message for the user that explains what kind of credentials are expected.<br/><br/>Please note that it is strongly recommended to always show the login hint to the user if there is one, as the credentials that finAPI requires for the bank might be different to the credentials that the user knows from the bank's website.<br/><br/>Also note that the contents of this field should always be interpreted as HTML, as the text might contain HTML tags for highlighted words, paragraphs, etc.  # noqa: E501

        :return: The login_hint of this Bank.  # noqa: E501
        :rtype: str
        """
        return self._login_hint

    @login_hint.setter
    def login_hint(self, login_hint):
        """Sets the login_hint of this Bank.

        Login hint. Contains a German message for the user that explains what kind of credentials are expected.<br/><br/>Please note that it is strongly recommended to always show the login hint to the user if there is one, as the credentials that finAPI requires for the bank might be different to the credentials that the user knows from the bank's website.<br/><br/>Also note that the contents of this field should always be interpreted as HTML, as the text might contain HTML tags for highlighted words, paragraphs, etc.  # noqa: E501

        :param login_hint: The login_hint of this Bank.  # noqa: E501
        :type: str
        """

        self._login_hint = login_hint

    @property
    def bic(self):
        """Gets the bic of this Bank.  # noqa: E501

        BIC of bank  # noqa: E501

        :return: The bic of this Bank.  # noqa: E501
        :rtype: str
        """
        return self._bic

    @bic.setter
    def bic(self, bic):
        """Sets the bic of this Bank.

        BIC of bank  # noqa: E501

        :param bic: The bic of this Bank.  # noqa: E501
        :type: str
        """

        self._bic = bic

    @property
    def blz(self):
        """Gets the blz of this Bank.  # noqa: E501

        BLZ of bank  # noqa: E501

        :return: The blz of this Bank.  # noqa: E501
        :rtype: str
        """
        return self._blz

    @blz.setter
    def blz(self, blz):
        """Sets the blz of this Bank.

        BLZ of bank  # noqa: E501

        :param blz: The blz of this Bank.  # noqa: E501
        :type: str
        """
        if blz is None:
            raise ValueError("Invalid value for `blz`, must not be `None`")  # noqa: E501

        self._blz = blz

    @property
    def blzs(self):
        """Gets the blzs of this Bank.  # noqa: E501

        List of BLZs that belong to this bank. NOTE: This field is deprecated and will be removed at some point. Please refer to field 'blz' instead.  # noqa: E501

        :return: The blzs of this Bank.  # noqa: E501
        :rtype: list[str]
        """
        return self._blzs

    @blzs.setter
    def blzs(self, blzs):
        """Sets the blzs of this Bank.

        List of BLZs that belong to this bank. NOTE: This field is deprecated and will be removed at some point. Please refer to field 'blz' instead.  # noqa: E501

        :param blzs: The blzs of this Bank.  # noqa: E501
        :type: list[str]
        """
        if blzs is None:
            raise ValueError("Invalid value for `blzs`, must not be `None`")  # noqa: E501

        self._blzs = blzs

    @property
    def login_field_user_id(self):
        """Gets the login_field_user_id of this Bank.  # noqa: E501

        Label for the user ID login field, as it is called on the bank's website (e.g. \"Nutzerkennung\"). If this field is set (i.e. not null) then you should prompt your users to enter the required data in a text field which you can label with this field's value.  # noqa: E501

        :return: The login_field_user_id of this Bank.  # noqa: E501
        :rtype: str
        """
        return self._login_field_user_id

    @login_field_user_id.setter
    def login_field_user_id(self, login_field_user_id):
        """Sets the login_field_user_id of this Bank.

        Label for the user ID login field, as it is called on the bank's website (e.g. \"Nutzerkennung\"). If this field is set (i.e. not null) then you should prompt your users to enter the required data in a text field which you can label with this field's value.  # noqa: E501

        :param login_field_user_id: The login_field_user_id of this Bank.  # noqa: E501
        :type: str
        """

        self._login_field_user_id = login_field_user_id

    @property
    def login_field_customer_id(self):
        """Gets the login_field_customer_id of this Bank.  # noqa: E501

        Label for the customer ID login field, as it is called on the bank's website (e.g. \"Kundennummer\"). If this field is set (i.e. not null) then you should prompt your users to enter the required data in a text field which you can label with this field's value.  # noqa: E501

        :return: The login_field_customer_id of this Bank.  # noqa: E501
        :rtype: str
        """
        return self._login_field_customer_id

    @login_field_customer_id.setter
    def login_field_customer_id(self, login_field_customer_id):
        """Sets the login_field_customer_id of this Bank.

        Label for the customer ID login field, as it is called on the bank's website (e.g. \"Kundennummer\"). If this field is set (i.e. not null) then you should prompt your users to enter the required data in a text field which you can label with this field's value.  # noqa: E501

        :param login_field_customer_id: The login_field_customer_id of this Bank.  # noqa: E501
        :type: str
        """

        self._login_field_customer_id = login_field_customer_id

    @property
    def login_field_pin(self):
        """Gets the login_field_pin of this Bank.  # noqa: E501

        Label for the PIN field, as it is called on the bank's website (mostly \"PIN\"). If this field is set (i.e. not null) then you should prompt your users to enter the required data in a text field which you can label with this field's value.  # noqa: E501

        :return: The login_field_pin of this Bank.  # noqa: E501
        :rtype: str
        """
        return self._login_field_pin

    @login_field_pin.setter
    def login_field_pin(self, login_field_pin):
        """Sets the login_field_pin of this Bank.

        Label for the PIN field, as it is called on the bank's website (mostly \"PIN\"). If this field is set (i.e. not null) then you should prompt your users to enter the required data in a text field which you can label with this field's value.  # noqa: E501

        :param login_field_pin: The login_field_pin of this Bank.  # noqa: E501
        :type: str
        """

        self._login_field_pin = login_field_pin

    @property
    def is_supported(self):
        """Gets the is_supported of this Bank.  # noqa: E501

        Whether this bank is supported by finAPI, i.e. whether you can import/update a bank connection of this bank.  # noqa: E501

        :return: The is_supported of this Bank.  # noqa: E501
        :rtype: bool
        """
        return self._is_supported

    @is_supported.setter
    def is_supported(self, is_supported):
        """Sets the is_supported of this Bank.

        Whether this bank is supported by finAPI, i.e. whether you can import/update a bank connection of this bank.  # noqa: E501

        :param is_supported: The is_supported of this Bank.  # noqa: E501
        :type: bool
        """
        if is_supported is None:
            raise ValueError("Invalid value for `is_supported`, must not be `None`")  # noqa: E501

        self._is_supported = is_supported

    @property
    def supported_data_sources(self):
        """Gets the supported_data_sources of this Bank.  # noqa: E501

        List of the data sources that finAPI will use for data download for this bank. Possible values:</br></br>&bull; <code>FINTS_SERVER</code> - means that finAPI will download data via the bank's FinTS interface.</br>&bull; <code>WEB_SCRAPER</code> - means that finAPI will parse data from the bank's online banking website.</br></br>Note that this list will be empty for non-supported banks. Note also that web scraping might be disabled for your client (see GET /clientConfiguration). When this is the case, then finAPI will not use the web scraper for data download, and if the web scraper is the only supported data source of this bank, then finAPI will not allow to download any data for this bank at all (for details, see POST /bankConnections/import and POST /bankConnections/update).  # noqa: E501

        :return: The supported_data_sources of this Bank.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_data_sources

    @supported_data_sources.setter
    def supported_data_sources(self, supported_data_sources):
        """Sets the supported_data_sources of this Bank.

        List of the data sources that finAPI will use for data download for this bank. Possible values:</br></br>&bull; <code>FINTS_SERVER</code> - means that finAPI will download data via the bank's FinTS interface.</br>&bull; <code>WEB_SCRAPER</code> - means that finAPI will parse data from the bank's online banking website.</br></br>Note that this list will be empty for non-supported banks. Note also that web scraping might be disabled for your client (see GET /clientConfiguration). When this is the case, then finAPI will not use the web scraper for data download, and if the web scraper is the only supported data source of this bank, then finAPI will not allow to download any data for this bank at all (for details, see POST /bankConnections/import and POST /bankConnections/update).  # noqa: E501

        :param supported_data_sources: The supported_data_sources of this Bank.  # noqa: E501
        :type: list[str]
        """
        if supported_data_sources is None:
            raise ValueError("Invalid value for `supported_data_sources`, must not be `None`")  # noqa: E501
        allowed_values = ["WEB_SCRAPER", "FINTS_SERVER"]  # noqa: E501
        if not set(supported_data_sources).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `supported_data_sources` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(supported_data_sources) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._supported_data_sources = supported_data_sources

    @property
    def pins_are_volatile(self):
        """Gets the pins_are_volatile of this Bank.  # noqa: E501

        Whether the PINs that are used for authentication with the bank are volatile. If the PINs are volatile, it means that a PIN is usually valid only for a single authentication, and is then invalidated. If a bank uses volatile PINs, it is strongly inadvisable to store PINs in finAPI, as a stored PIN will not work for future authentications.  # noqa: E501

        :return: The pins_are_volatile of this Bank.  # noqa: E501
        :rtype: bool
        """
        return self._pins_are_volatile

    @pins_are_volatile.setter
    def pins_are_volatile(self, pins_are_volatile):
        """Sets the pins_are_volatile of this Bank.

        Whether the PINs that are used for authentication with the bank are volatile. If the PINs are volatile, it means that a PIN is usually valid only for a single authentication, and is then invalidated. If a bank uses volatile PINs, it is strongly inadvisable to store PINs in finAPI, as a stored PIN will not work for future authentications.  # noqa: E501

        :param pins_are_volatile: The pins_are_volatile of this Bank.  # noqa: E501
        :type: bool
        """
        if pins_are_volatile is None:
            raise ValueError("Invalid value for `pins_are_volatile`, must not be `None`")  # noqa: E501

        self._pins_are_volatile = pins_are_volatile

    @property
    def location(self):
        """Gets the location of this Bank.  # noqa: E501

        Bank location (two-letter country code; ISO 3166 ALPHA-2). Note that when this field is not set, it means that this bank depicts an international institute which is not bound to any specific country.  # noqa: E501

        :return: The location of this Bank.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Bank.

        Bank location (two-letter country code; ISO 3166 ALPHA-2). Note that when this field is not set, it means that this bank depicts an international institute which is not bound to any specific country.  # noqa: E501

        :param location: The location of this Bank.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def city(self):
        """Gets the city of this Bank.  # noqa: E501

        City that this bank is located in. Note that this field may not be set for some banks.  # noqa: E501

        :return: The city of this Bank.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Bank.

        City that this bank is located in. Note that this field may not be set for some banks.  # noqa: E501

        :param city: The city of this Bank.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def is_test_bank(self):
        """Gets the is_test_bank of this Bank.  # noqa: E501

        If true, then this bank does not depict a real bank, but rather a testing endpoint provided by a bank or by finAPI. You probably want to regard these banks only during the development of your application, but not in production. You can filter out these banks in production by making sure that the 'isTestBank' parameter is always set to 'false' whenever your application is calling the 'Get and search all banks' service.  # noqa: E501

        :return: The is_test_bank of this Bank.  # noqa: E501
        :rtype: bool
        """
        return self._is_test_bank

    @is_test_bank.setter
    def is_test_bank(self, is_test_bank):
        """Sets the is_test_bank of this Bank.

        If true, then this bank does not depict a real bank, but rather a testing endpoint provided by a bank or by finAPI. You probably want to regard these banks only during the development of your application, but not in production. You can filter out these banks in production by making sure that the 'isTestBank' parameter is always set to 'false' whenever your application is calling the 'Get and search all banks' service.  # noqa: E501

        :param is_test_bank: The is_test_bank of this Bank.  # noqa: E501
        :type: bool
        """
        if is_test_bank is None:
            raise ValueError("Invalid value for `is_test_bank`, must not be `None`")  # noqa: E501

        self._is_test_bank = is_test_bank

    @property
    def popularity(self):
        """Gets the popularity of this Bank.  # noqa: E501

        Popularity of this bank with your users (mandator-wide, i.e. across all of your clients). The value equals the number of bank connections that are currently imported for this bank across all of your users (which means it is a constantly adjusting value). You can use this field for statistical evaluation, and also for ordering bank search results (see service 'Get and search all banks').  # noqa: E501

        :return: The popularity of this Bank.  # noqa: E501
        :rtype: int
        """
        return self._popularity

    @popularity.setter
    def popularity(self, popularity):
        """Sets the popularity of this Bank.

        Popularity of this bank with your users (mandator-wide, i.e. across all of your clients). The value equals the number of bank connections that are currently imported for this bank across all of your users (which means it is a constantly adjusting value). You can use this field for statistical evaluation, and also for ordering bank search results (see service 'Get and search all banks').  # noqa: E501

        :param popularity: The popularity of this Bank.  # noqa: E501
        :type: int
        """
        if popularity is None:
            raise ValueError("Invalid value for `popularity`, must not be `None`")  # noqa: E501

        self._popularity = popularity

    @property
    def health(self):
        """Gets the health of this Bank.  # noqa: E501

        The health status of this bank. This is a value between 0 and 100, depicting the percentage of successful communication attempts with this bank during the latest couple of bank connection imports or updates (across the entire finAPI system). Note that 'successful' means that there was no technical error trying to establish a communication with the bank. Non-technical errors (like incorrect credentials) are regarded successful communication attempts.  # noqa: E501

        :return: The health of this Bank.  # noqa: E501
        :rtype: int
        """
        return self._health

    @health.setter
    def health(self, health):
        """Sets the health of this Bank.

        The health status of this bank. This is a value between 0 and 100, depicting the percentage of successful communication attempts with this bank during the latest couple of bank connection imports or updates (across the entire finAPI system). Note that 'successful' means that there was no technical error trying to establish a communication with the bank. Non-technical errors (like incorrect credentials) are regarded successful communication attempts.  # noqa: E501

        :param health: The health of this Bank.  # noqa: E501
        :type: int
        """
        if health is None:
            raise ValueError("Invalid value for `health`, must not be `None`")  # noqa: E501
        if health is not None and health > 100:  # noqa: E501
            raise ValueError("Invalid value for `health`, must be a value less than or equal to `100`")  # noqa: E501
        if health is not None and health < 0:  # noqa: E501
            raise ValueError("Invalid value for `health`, must be a value greater than or equal to `0`")  # noqa: E501

        self._health = health

    @property
    def last_communication_attempt(self):
        """Gets the last_communication_attempt of this Bank.  # noqa: E501

        Time of the last communication attempt with this bank during a bank connection import or update (across the entire finAPI system). The value is returned in the format 'yyyy-MM-dd HH:mm:ss.SSS' (german time).  # noqa: E501

        :return: The last_communication_attempt of this Bank.  # noqa: E501
        :rtype: str
        """
        return self._last_communication_attempt

    @last_communication_attempt.setter
    def last_communication_attempt(self, last_communication_attempt):
        """Sets the last_communication_attempt of this Bank.

        Time of the last communication attempt with this bank during a bank connection import or update (across the entire finAPI system). The value is returned in the format 'yyyy-MM-dd HH:mm:ss.SSS' (german time).  # noqa: E501

        :param last_communication_attempt: The last_communication_attempt of this Bank.  # noqa: E501
        :type: str
        """

        self._last_communication_attempt = last_communication_attempt

    @property
    def last_successful_communication(self):
        """Gets the last_successful_communication of this Bank.  # noqa: E501

        Time of the last successful communication with this bank during a bank connection import or update (across the entire finAPI system). The value is returned in the format 'yyyy-MM-dd HH:mm:ss.SSS' (german time).  # noqa: E501

        :return: The last_successful_communication of this Bank.  # noqa: E501
        :rtype: str
        """
        return self._last_successful_communication

    @last_successful_communication.setter
    def last_successful_communication(self, last_successful_communication):
        """Sets the last_successful_communication of this Bank.

        Time of the last successful communication with this bank during a bank connection import or update (across the entire finAPI system). The value is returned in the format 'yyyy-MM-dd HH:mm:ss.SSS' (german time).  # noqa: E501

        :param last_successful_communication: The last_successful_communication of this Bank.  # noqa: E501
        :type: str
        """

        self._last_successful_communication = last_successful_communication

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
        if not isinstance(other, Bank):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
