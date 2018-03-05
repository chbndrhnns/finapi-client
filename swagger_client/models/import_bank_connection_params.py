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


class ImportBankConnectionParams(object):
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
        'bank_id': 'int',
        'banking_user_id': 'str',
        'banking_customer_id': 'str',
        'banking_pin': 'str',
        'store_pin': 'bool',
        'name': 'str',
        'skip_positions_download': 'bool',
        'max_days_for_download': 'int',
        'account_type_ids': 'list[int]',
        'challenge_response': 'str'
    }

    attribute_map = {
        'bank_id': 'bankId',
        'banking_user_id': 'bankingUserId',
        'banking_customer_id': 'bankingCustomerId',
        'banking_pin': 'bankingPin',
        'store_pin': 'storePin',
        'name': 'name',
        'skip_positions_download': 'skipPositionsDownload',
        'max_days_for_download': 'maxDaysForDownload',
        'account_type_ids': 'accountTypeIds',
        'challenge_response': 'challengeResponse'
    }

    def __init__(self, bank_id=None, banking_user_id=None, banking_customer_id=None, banking_pin=None, store_pin=False, name=None, skip_positions_download=False, max_days_for_download=None, account_type_ids=None, challenge_response=None):  # noqa: E501
        """ImportBankConnectionParams - a model defined in Swagger"""  # noqa: E501

        self._bank_id = None
        self._banking_user_id = None
        self._banking_customer_id = None
        self._banking_pin = None
        self._store_pin = None
        self._name = None
        self._skip_positions_download = None
        self._max_days_for_download = None
        self._account_type_ids = None
        self._challenge_response = None
        self.discriminator = None

        self.bank_id = bank_id
        if banking_user_id is not None:
            self.banking_user_id = banking_user_id
        if banking_customer_id is not None:
            self.banking_customer_id = banking_customer_id
        if banking_pin is not None:
            self.banking_pin = banking_pin
        if store_pin is not None:
            self.store_pin = store_pin
        if name is not None:
            self.name = name
        if skip_positions_download is not None:
            self.skip_positions_download = skip_positions_download
        if max_days_for_download is not None:
            self.max_days_for_download = max_days_for_download
        if account_type_ids is not None:
            self.account_type_ids = account_type_ids
        if challenge_response is not None:
            self.challenge_response = challenge_response

    @property
    def bank_id(self):
        """Gets the bank_id of this ImportBankConnectionParams.  # noqa: E501

        Bank Identifier  # noqa: E501

        :return: The bank_id of this ImportBankConnectionParams.  # noqa: E501
        :rtype: int
        """
        return self._bank_id

    @bank_id.setter
    def bank_id(self, bank_id):
        """Sets the bank_id of this ImportBankConnectionParams.

        Bank Identifier  # noqa: E501

        :param bank_id: The bank_id of this ImportBankConnectionParams.  # noqa: E501
        :type: int
        """
        if bank_id is None:
            raise ValueError("Invalid value for `bank_id`, must not be `None`")  # noqa: E501

        self._bank_id = bank_id

    @property
    def banking_user_id(self):
        """Gets the banking_user_id of this ImportBankConnectionParams.  # noqa: E501

        Online banking user ID credential. When importing the 'demo connection', you may leave this field unset. Max length: 64.  # noqa: E501

        :return: The banking_user_id of this ImportBankConnectionParams.  # noqa: E501
        :rtype: str
        """
        return self._banking_user_id

    @banking_user_id.setter
    def banking_user_id(self, banking_user_id):
        """Sets the banking_user_id of this ImportBankConnectionParams.

        Online banking user ID credential. When importing the 'demo connection', you may leave this field unset. Max length: 64.  # noqa: E501

        :param banking_user_id: The banking_user_id of this ImportBankConnectionParams.  # noqa: E501
        :type: str
        """

        self._banking_user_id = banking_user_id

    @property
    def banking_customer_id(self):
        """Gets the banking_customer_id of this ImportBankConnectionParams.  # noqa: E501

        Online banking customer ID credential (for most banks this field can remain unset). Max length: 64.  # noqa: E501

        :return: The banking_customer_id of this ImportBankConnectionParams.  # noqa: E501
        :rtype: str
        """
        return self._banking_customer_id

    @banking_customer_id.setter
    def banking_customer_id(self, banking_customer_id):
        """Sets the banking_customer_id of this ImportBankConnectionParams.

        Online banking customer ID credential (for most banks this field can remain unset). Max length: 64.  # noqa: E501

        :param banking_customer_id: The banking_customer_id of this ImportBankConnectionParams.  # noqa: E501
        :type: str
        """

        self._banking_customer_id = banking_customer_id

    @property
    def banking_pin(self):
        """Gets the banking_pin of this ImportBankConnectionParams.  # noqa: E501

        Online banking PIN. When importing the 'demo connection', you may leave this field unset. Any symbols are allowed. Max length: 170.  # noqa: E501

        :return: The banking_pin of this ImportBankConnectionParams.  # noqa: E501
        :rtype: str
        """
        return self._banking_pin

    @banking_pin.setter
    def banking_pin(self, banking_pin):
        """Sets the banking_pin of this ImportBankConnectionParams.

        Online banking PIN. When importing the 'demo connection', you may leave this field unset. Any symbols are allowed. Max length: 170.  # noqa: E501

        :param banking_pin: The banking_pin of this ImportBankConnectionParams.  # noqa: E501
        :type: str
        """

        self._banking_pin = banking_pin

    @property
    def store_pin(self):
        """Gets the store_pin of this ImportBankConnectionParams.  # noqa: E501

        Whether to store the PIN. If the PIN is stored, it is not required to pass the PIN again when updating this bank connection or executing orders (like money transfers). Default is false. <br/><br/>NOTE: Before you set this field to true, please regard the 'pinsAreVolatile' flag of this connection's bank.  # noqa: E501

        :return: The store_pin of this ImportBankConnectionParams.  # noqa: E501
        :rtype: bool
        """
        return self._store_pin

    @store_pin.setter
    def store_pin(self, store_pin):
        """Sets the store_pin of this ImportBankConnectionParams.

        Whether to store the PIN. If the PIN is stored, it is not required to pass the PIN again when updating this bank connection or executing orders (like money transfers). Default is false. <br/><br/>NOTE: Before you set this field to true, please regard the 'pinsAreVolatile' flag of this connection's bank.  # noqa: E501

        :param store_pin: The store_pin of this ImportBankConnectionParams.  # noqa: E501
        :type: bool
        """

        self._store_pin = store_pin

    @property
    def name(self):
        """Gets the name of this ImportBankConnectionParams.  # noqa: E501

        Custom name for the bank connection. Maximum length is 64. If you do not want to set a name, you can leave this field unset.  # noqa: E501

        :return: The name of this ImportBankConnectionParams.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImportBankConnectionParams.

        Custom name for the bank connection. Maximum length is 64. If you do not want to set a name, you can leave this field unset.  # noqa: E501

        :param name: The name of this ImportBankConnectionParams.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def skip_positions_download(self):
        """Gets the skip_positions_download of this ImportBankConnectionParams.  # noqa: E501

        Whether to skip the download of transactions and securities or not. If set to true, then finAPI will download just the accounts list with the accounts' information (like account name, number, holder, etc), as well as the accounts' balances (if possible), but skip the download of transactions and securities. Default is false.<br/><br/>NOTES:<br/>&bull; If you skip the download of transactions and securities during an import or update, you can still download them on a later update (though you might not get all positions at a later point, because the date range in which the bank servers provide this data is usually limited). However, once finAPI has downloaded the transactions or securities for the first time, you will not be able to go back to skipping the download of transactions and securities! In other words: Once you make your first request with skipPositionsDownload=false for a certain bank connection, you will no longer be able to make a request with skipPositionsDownload=true for that same bank connection.<br/>&bull; If this bank connection is updated via finAPI's automatic batch update, then transactions and security positions <u>will</u> be downloaded in any case!<br/>&bull; For security accounts, skipping the downloading of the securities might result in the account's balance also not being downloaded.<br/>&bull; For Bausparen accounts, this field is ignored. finAPI will always download transactions for Bausparen accounts.<br/><br/><b>This flag is currently not guaranteed to work for non-German banks!</b>  # noqa: E501

        :return: The skip_positions_download of this ImportBankConnectionParams.  # noqa: E501
        :rtype: bool
        """
        return self._skip_positions_download

    @skip_positions_download.setter
    def skip_positions_download(self, skip_positions_download):
        """Sets the skip_positions_download of this ImportBankConnectionParams.

        Whether to skip the download of transactions and securities or not. If set to true, then finAPI will download just the accounts list with the accounts' information (like account name, number, holder, etc), as well as the accounts' balances (if possible), but skip the download of transactions and securities. Default is false.<br/><br/>NOTES:<br/>&bull; If you skip the download of transactions and securities during an import or update, you can still download them on a later update (though you might not get all positions at a later point, because the date range in which the bank servers provide this data is usually limited). However, once finAPI has downloaded the transactions or securities for the first time, you will not be able to go back to skipping the download of transactions and securities! In other words: Once you make your first request with skipPositionsDownload=false for a certain bank connection, you will no longer be able to make a request with skipPositionsDownload=true for that same bank connection.<br/>&bull; If this bank connection is updated via finAPI's automatic batch update, then transactions and security positions <u>will</u> be downloaded in any case!<br/>&bull; For security accounts, skipping the downloading of the securities might result in the account's balance also not being downloaded.<br/>&bull; For Bausparen accounts, this field is ignored. finAPI will always download transactions for Bausparen accounts.<br/><br/><b>This flag is currently not guaranteed to work for non-German banks!</b>  # noqa: E501

        :param skip_positions_download: The skip_positions_download of this ImportBankConnectionParams.  # noqa: E501
        :type: bool
        """

        self._skip_positions_download = skip_positions_download

    @property
    def max_days_for_download(self):
        """Gets the max_days_for_download of this ImportBankConnectionParams.  # noqa: E501

        Use this parameter if you want to limit the date range for transactions download. The value depicts the number of days that finAPI will download transactions for, starting from - and including - today. For example, if you want to download only transactions from within the past 30 days (including today), then pass the value 30. The minimum allowed value is 14, the maximum value is 3650. You may also pass the value 0 though (which is also the default value when you do not specify this parameter), in which case there will be no limit to the transactions download and finAPI will try to get all transactions that it can. Please note that when you specify the parameter there is no guarantee that finAPI will actually download transactions for the entire given date range, as the bank servers may limit the date range on their own. Also note that this parameter only applies to transactions, not to security positions; finAPI will always download all positions that it can get. At last, please note that this parameter is ignored when importing the 'demo connection'.<br/><br/><b>This flag is currently not guaranteed to work for non-German banks!</b>  # noqa: E501

        :return: The max_days_for_download of this ImportBankConnectionParams.  # noqa: E501
        :rtype: int
        """
        return self._max_days_for_download

    @max_days_for_download.setter
    def max_days_for_download(self, max_days_for_download):
        """Sets the max_days_for_download of this ImportBankConnectionParams.

        Use this parameter if you want to limit the date range for transactions download. The value depicts the number of days that finAPI will download transactions for, starting from - and including - today. For example, if you want to download only transactions from within the past 30 days (including today), then pass the value 30. The minimum allowed value is 14, the maximum value is 3650. You may also pass the value 0 though (which is also the default value when you do not specify this parameter), in which case there will be no limit to the transactions download and finAPI will try to get all transactions that it can. Please note that when you specify the parameter there is no guarantee that finAPI will actually download transactions for the entire given date range, as the bank servers may limit the date range on their own. Also note that this parameter only applies to transactions, not to security positions; finAPI will always download all positions that it can get. At last, please note that this parameter is ignored when importing the 'demo connection'.<br/><br/><b>This flag is currently not guaranteed to work for non-German banks!</b>  # noqa: E501

        :param max_days_for_download: The max_days_for_download of this ImportBankConnectionParams.  # noqa: E501
        :type: int
        """

        self._max_days_for_download = max_days_for_download

    @property
    def account_type_ids(self):
        """Gets the account_type_ids of this ImportBankConnectionParams.  # noqa: E501

        Whitelist of identifiers of finAPI account types that are considered for the import. Only accounts whose type matches with one of the given types will be imported. Note that when the bank connection does not contain any accounts of the given types, the import will fail with error code NO_ACCOUNTS_FOR_TYPE_LIST. If no whitelist is given, then all accounts will be imported.<br/><br/><br/>1 = Checking,<br/>2 = Savings,<br/>3 = CreditCard,<br/>4 = Security,<br/>5 = Loan,<br/>6 = Pocket (DEPRECATED; will not be returned for any account unless this type has explicitly been set via PATCH),<br/>7 = Membership,<br/>8 = Bausparen<br/><br/><b>This flag is currently not guaranteed to work for non-German banks!</b>  # noqa: E501

        :return: The account_type_ids of this ImportBankConnectionParams.  # noqa: E501
        :rtype: list[int]
        """
        return self._account_type_ids

    @account_type_ids.setter
    def account_type_ids(self, account_type_ids):
        """Sets the account_type_ids of this ImportBankConnectionParams.

        Whitelist of identifiers of finAPI account types that are considered for the import. Only accounts whose type matches with one of the given types will be imported. Note that when the bank connection does not contain any accounts of the given types, the import will fail with error code NO_ACCOUNTS_FOR_TYPE_LIST. If no whitelist is given, then all accounts will be imported.<br/><br/><br/>1 = Checking,<br/>2 = Savings,<br/>3 = CreditCard,<br/>4 = Security,<br/>5 = Loan,<br/>6 = Pocket (DEPRECATED; will not be returned for any account unless this type has explicitly been set via PATCH),<br/>7 = Membership,<br/>8 = Bausparen<br/><br/><b>This flag is currently not guaranteed to work for non-German banks!</b>  # noqa: E501

        :param account_type_ids: The account_type_ids of this ImportBankConnectionParams.  # noqa: E501
        :type: list[int]
        """

        self._account_type_ids = account_type_ids

    @property
    def challenge_response(self):
        """Gets the challenge_response of this ImportBankConnectionParams.  # noqa: E501

        Challenge response. This field should be set only when the previous attempt of importing the bank connection failed with HTTP code 510, i.e. the bank sent a challenge for the user for an additional authentication. In this case, this field must contain the response to the bank's challenge.  # noqa: E501

        :return: The challenge_response of this ImportBankConnectionParams.  # noqa: E501
        :rtype: str
        """
        return self._challenge_response

    @challenge_response.setter
    def challenge_response(self, challenge_response):
        """Sets the challenge_response of this ImportBankConnectionParams.

        Challenge response. This field should be set only when the previous attempt of importing the bank connection failed with HTTP code 510, i.e. the bank sent a challenge for the user for an additional authentication. In this case, this field must contain the response to the bank's challenge.  # noqa: E501

        :param challenge_response: The challenge_response of this ImportBankConnectionParams.  # noqa: E501
        :type: str
        """

        self._challenge_response = challenge_response

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
        if not isinstance(other, ImportBankConnectionParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other