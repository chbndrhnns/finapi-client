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

from swagger_client.models.monthly_user_stats import MonthlyUserStats  # noqa: F401,E501


class UserInfo(object):
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
        'user_id': 'str',
        'registration_date': 'str',
        'deletion_date': 'str',
        'last_active_date': 'str',
        'bank_connection_count': 'int',
        'latest_bank_connection_import_date': 'str',
        'latest_bank_connection_deletion_date': 'str',
        'monthly_stats': 'list[MonthlyUserStats]'
    }

    attribute_map = {
        'user_id': 'userId',
        'registration_date': 'registrationDate',
        'deletion_date': 'deletionDate',
        'last_active_date': 'lastActiveDate',
        'bank_connection_count': 'bankConnectionCount',
        'latest_bank_connection_import_date': 'latestBankConnectionImportDate',
        'latest_bank_connection_deletion_date': 'latestBankConnectionDeletionDate',
        'monthly_stats': 'monthlyStats'
    }

    def __init__(self, user_id=None, registration_date=None, deletion_date=None, last_active_date=None, bank_connection_count=None, latest_bank_connection_import_date=None, latest_bank_connection_deletion_date=None, monthly_stats=None):  # noqa: E501
        """UserInfo - a model defined in Swagger"""  # noqa: E501

        self._user_id = None
        self._registration_date = None
        self._deletion_date = None
        self._last_active_date = None
        self._bank_connection_count = None
        self._latest_bank_connection_import_date = None
        self._latest_bank_connection_deletion_date = None
        self._monthly_stats = None
        self.discriminator = None

        self.user_id = user_id
        self.registration_date = registration_date
        if deletion_date is not None:
            self.deletion_date = deletion_date
        if last_active_date is not None:
            self.last_active_date = last_active_date
        self.bank_connection_count = bank_connection_count
        if latest_bank_connection_import_date is not None:
            self.latest_bank_connection_import_date = latest_bank_connection_import_date
        if latest_bank_connection_deletion_date is not None:
            self.latest_bank_connection_deletion_date = latest_bank_connection_deletion_date
        if monthly_stats is not None:
            self.monthly_stats = monthly_stats

    @property
    def user_id(self):
        """Gets the user_id of this UserInfo.  # noqa: E501

        User's identifier  # noqa: E501

        :return: The user_id of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserInfo.

        User's identifier  # noqa: E501

        :param user_id: The user_id of this UserInfo.  # noqa: E501
        :type: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

    @property
    def registration_date(self):
        """Gets the registration_date of this UserInfo.  # noqa: E501

        User's registration date, in the format 'yyyy-MM-dd'  # noqa: E501

        :return: The registration_date of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._registration_date

    @registration_date.setter
    def registration_date(self, registration_date):
        """Sets the registration_date of this UserInfo.

        User's registration date, in the format 'yyyy-MM-dd'  # noqa: E501

        :param registration_date: The registration_date of this UserInfo.  # noqa: E501
        :type: str
        """
        if registration_date is None:
            raise ValueError("Invalid value for `registration_date`, must not be `None`")  # noqa: E501

        self._registration_date = registration_date

    @property
    def deletion_date(self):
        """Gets the deletion_date of this UserInfo.  # noqa: E501

        User's deletion date, in the format 'yyyy-MM-dd'. May be null if the user has not been deleted.  # noqa: E501

        :return: The deletion_date of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._deletion_date

    @deletion_date.setter
    def deletion_date(self, deletion_date):
        """Sets the deletion_date of this UserInfo.

        User's deletion date, in the format 'yyyy-MM-dd'. May be null if the user has not been deleted.  # noqa: E501

        :param deletion_date: The deletion_date of this UserInfo.  # noqa: E501
        :type: str
        """

        self._deletion_date = deletion_date

    @property
    def last_active_date(self):
        """Gets the last_active_date of this UserInfo.  # noqa: E501

        User's last active date, in the format 'yyyy-MM-dd'. May be null if the user has not yet logged in.  # noqa: E501

        :return: The last_active_date of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._last_active_date

    @last_active_date.setter
    def last_active_date(self, last_active_date):
        """Sets the last_active_date of this UserInfo.

        User's last active date, in the format 'yyyy-MM-dd'. May be null if the user has not yet logged in.  # noqa: E501

        :param last_active_date: The last_active_date of this UserInfo.  # noqa: E501
        :type: str
        """

        self._last_active_date = last_active_date

    @property
    def bank_connection_count(self):
        """Gets the bank_connection_count of this UserInfo.  # noqa: E501

        Number of bank connections that currently exist for this user.  # noqa: E501

        :return: The bank_connection_count of this UserInfo.  # noqa: E501
        :rtype: int
        """
        return self._bank_connection_count

    @bank_connection_count.setter
    def bank_connection_count(self, bank_connection_count):
        """Sets the bank_connection_count of this UserInfo.

        Number of bank connections that currently exist for this user.  # noqa: E501

        :param bank_connection_count: The bank_connection_count of this UserInfo.  # noqa: E501
        :type: int
        """
        if bank_connection_count is None:
            raise ValueError("Invalid value for `bank_connection_count`, must not be `None`")  # noqa: E501

        self._bank_connection_count = bank_connection_count

    @property
    def latest_bank_connection_import_date(self):
        """Gets the latest_bank_connection_import_date of this UserInfo.  # noqa: E501

        Latest date of when a bank connection was imported for this user, in the format 'yyyy-MM-dd'. This field is null when there has never been a bank connection import.  # noqa: E501

        :return: The latest_bank_connection_import_date of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._latest_bank_connection_import_date

    @latest_bank_connection_import_date.setter
    def latest_bank_connection_import_date(self, latest_bank_connection_import_date):
        """Sets the latest_bank_connection_import_date of this UserInfo.

        Latest date of when a bank connection was imported for this user, in the format 'yyyy-MM-dd'. This field is null when there has never been a bank connection import.  # noqa: E501

        :param latest_bank_connection_import_date: The latest_bank_connection_import_date of this UserInfo.  # noqa: E501
        :type: str
        """

        self._latest_bank_connection_import_date = latest_bank_connection_import_date

    @property
    def latest_bank_connection_deletion_date(self):
        """Gets the latest_bank_connection_deletion_date of this UserInfo.  # noqa: E501

        Latest date of when a bank connection was deleted for this user, in the format 'yyyy-MM-dd'. This field is null when there has never been a bank connection deletion.  # noqa: E501

        :return: The latest_bank_connection_deletion_date of this UserInfo.  # noqa: E501
        :rtype: str
        """
        return self._latest_bank_connection_deletion_date

    @latest_bank_connection_deletion_date.setter
    def latest_bank_connection_deletion_date(self, latest_bank_connection_deletion_date):
        """Sets the latest_bank_connection_deletion_date of this UserInfo.

        Latest date of when a bank connection was deleted for this user, in the format 'yyyy-MM-dd'. This field is null when there has never been a bank connection deletion.  # noqa: E501

        :param latest_bank_connection_deletion_date: The latest_bank_connection_deletion_date of this UserInfo.  # noqa: E501
        :type: str
        """

        self._latest_bank_connection_deletion_date = latest_bank_connection_deletion_date

    @property
    def monthly_stats(self):
        """Gets the monthly_stats of this UserInfo.  # noqa: E501

        Additional information about the user's data or activities, broken down in months. The list will by default contain an entry for each month starting with the month of when the user was registered, up to the current month. The date range may vary when you have limited it in the request. <br/><br/>Please note:<br/>&bull; this field is only set when 'includeMonthlyStats' = true, otherwise it will be null.<br/>&bull; the list is always ordered from the latest month first, to the oldest month last.<br/>&bull; the list will never contain an entry for a month that was prior to the month of when the user was registered, or after the month of when the user was deleted, even when you have explicitly set a respective date range. This means that the list may be empty if you are requesting a date range where the user didn't exist yet, or didn't exist any longer.  # noqa: E501

        :return: The monthly_stats of this UserInfo.  # noqa: E501
        :rtype: list[MonthlyUserStats]
        """
        return self._monthly_stats

    @monthly_stats.setter
    def monthly_stats(self, monthly_stats):
        """Sets the monthly_stats of this UserInfo.

        Additional information about the user's data or activities, broken down in months. The list will by default contain an entry for each month starting with the month of when the user was registered, up to the current month. The date range may vary when you have limited it in the request. <br/><br/>Please note:<br/>&bull; this field is only set when 'includeMonthlyStats' = true, otherwise it will be null.<br/>&bull; the list is always ordered from the latest month first, to the oldest month last.<br/>&bull; the list will never contain an entry for a month that was prior to the month of when the user was registered, or after the month of when the user was deleted, even when you have explicitly set a respective date range. This means that the list may be empty if you are requesting a date range where the user didn't exist yet, or didn't exist any longer.  # noqa: E501

        :param monthly_stats: The monthly_stats of this UserInfo.  # noqa: E501
        :type: list[MonthlyUserStats]
        """

        self._monthly_stats = monthly_stats

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
        if not isinstance(other, UserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
