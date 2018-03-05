# coding: utf-8

"""
    finAPI RESTful Services

    finAPI RESTful Services  # noqa: E501

    OpenAPI spec version: v1.41.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class MandatorAdministrationApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_users(self, body, **kwargs):  # noqa: E501
        """Delete users  # noqa: E501

        Delete one or several users, which are specified by a given list of identifiers. Must pass the <a href='https://finapi.zendesk.com/hc/en-us/articles/115003661827-Difference-between-app-clients-and-mandator-admin-client'>mandator admin client</a>'s access_token. <br/><br/><b>NOTE</b>: finAPI may fail to delete one (or several, or all) of the specified users. A user cannot get deleted when his data is currently locked by an internal process (for instance, update of a bank connection or transactions categorization). The response contains the identifiers of all users that could not get deleted, and all users that could get deleted, separated in two lists. The mandator admin client can retry the request at a later time for the users who could not get deleted.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_users(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param UserIdentifiersParams body: List of user identifiers (required)
        :return: UserIdentifiersList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.delete_users_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_users_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def delete_users_with_http_info(self, body, **kwargs):  # noqa: E501
        """Delete users  # noqa: E501

        Delete one or several users, which are specified by a given list of identifiers. Must pass the <a href='https://finapi.zendesk.com/hc/en-us/articles/115003661827-Difference-between-app-clients-and-mandator-admin-client'>mandator admin client</a>'s access_token. <br/><br/><b>NOTE</b>: finAPI may fail to delete one (or several, or all) of the specified users. A user cannot get deleted when his data is currently locked by an internal process (for instance, update of a bank connection or transactions categorization). The response contains the identifiers of all users that could not get deleted, and all users that could get deleted, separated in two lists. The mandator admin client can retry the request at a later time for the users who could not get deleted.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_users_with_http_info(body, async=True)
        >>> result = thread.get()

        :param async bool
        :param UserIdentifiersParams body: List of user identifiers (required)
        :return: UserIdentifiersList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_users" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `delete_users`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['finapi_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/mandatorAdmin/deleteUsers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserIdentifiersList',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_user_list(self, **kwargs):  # noqa: E501
        """Get user list  # noqa: E501

        <p>Get a list of the users of the mandator that is authorized by the access_token. Must pass the <a href='https://finapi.zendesk.com/hc/en-us/articles/115003661827-Difference-between-app-clients-and-mandator-admin-client'>mandator admin client</a>'s access_token. You can set optional search criteria to get only those users that you are interested in. If you do not specify any search criteria, then this service functions as a 'get all' service.</p><p>Note that the original user id is longer available in finAPI once a user has been deleted. Because of this, the userId of deleted users will be a distorted version of the original userId. For example, if the deleted user's id was originally 'user', then this service will return 'uXXr' as the userId.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_user_list(async=True)
        >>> result = thread.get()

        :param async bool
        :param str min_registration_date: Lower bound for a user's registration date, in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). If specified, then only users whose 'registrationDate' is equal to or later than the given date will be regarded.
        :param str max_registration_date: Upper bound for a user's registration date, in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). If specified, then only users whose 'registrationDate' is equal to or earlier than the given date will be regarded.
        :param str min_deletion_date: Lower bound for a user's deletion date, in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). If specified, then only users whose 'deletionDate' is not null, and is equal to or later than the given date will be regarded.
        :param str max_deletion_date: Upper bound for a user's deletion date, in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). If specified, then only users whose 'deletionDate' is null, or is equal to or earlier than the given date will be regarded.
        :param str min_last_active_date: Lower bound for a user's last active date, in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). If specified, then only users whose 'lastActiveDate' is not null, and is equal to or later than the given date will be regarded.
        :param str max_last_active_date: Upper bound for a user's last active date, in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). If specified, then only users whose 'lastActiveDate' is null, or is equal to or earlier than the given date will be regarded.
        :param bool include_monthly_stats: Whether to include the 'monthlyStats' for the returned users. If not specified, then the field defaults to 'false'.
        :param str monthly_stats_start_date: Minimum bound for the monthly stats (=oldest month that should be included). Must be passed in the format 'YYYY-MM'. If not specified, then the monthly stats will go back up to the first month in which the user existed (date of the user's registration). Note that this field is only regarded if 'includeMonthlyStats' = true.
        :param str monthly_stats_end_date: Maximum bound for the monthly stats (=latest month that should be included). Must be passed in the format 'YYYY-MM'. If not specified, then the monthly stats will go up to either the current month (for active users), or up to the month of deletion (for deleted users). Note that this field is only regarded if  'includeMonthlyStats' = true.
        :param bool is_deleted: If NOT specified, then the service will regard both active and deleted users in the search. If set to 'true', then ONLY deleted users will be regarded. If set to 'false', then ONLY active users will be regarded.
        :param int page: Result page that you want to retrieve
        :param int per_page: Maximum number of records per page. Can be at most 500. NOTE: Due to its validation and visualization, the swagger frontend might show very low performance, or even crashes, when a service responds with a lot of data. It is recommended to use a HTTP client like Postman or DHC instead of our swagger frontend for service calls with large page sizes.
        :param list[str] order: Determines the order of the results. You can order the results by 'userId'. The default order for this service is 'userId,asc'. The general format is: 'property[,asc|desc]', with 'asc' being the default value. 
        :return: PageableUserInfoList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_user_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_user_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_user_list_with_http_info(self, **kwargs):  # noqa: E501
        """Get user list  # noqa: E501

        <p>Get a list of the users of the mandator that is authorized by the access_token. Must pass the <a href='https://finapi.zendesk.com/hc/en-us/articles/115003661827-Difference-between-app-clients-and-mandator-admin-client'>mandator admin client</a>'s access_token. You can set optional search criteria to get only those users that you are interested in. If you do not specify any search criteria, then this service functions as a 'get all' service.</p><p>Note that the original user id is longer available in finAPI once a user has been deleted. Because of this, the userId of deleted users will be a distorted version of the original userId. For example, if the deleted user's id was originally 'user', then this service will return 'uXXr' as the userId.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_user_list_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str min_registration_date: Lower bound for a user's registration date, in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). If specified, then only users whose 'registrationDate' is equal to or later than the given date will be regarded.
        :param str max_registration_date: Upper bound for a user's registration date, in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). If specified, then only users whose 'registrationDate' is equal to or earlier than the given date will be regarded.
        :param str min_deletion_date: Lower bound for a user's deletion date, in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). If specified, then only users whose 'deletionDate' is not null, and is equal to or later than the given date will be regarded.
        :param str max_deletion_date: Upper bound for a user's deletion date, in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). If specified, then only users whose 'deletionDate' is null, or is equal to or earlier than the given date will be regarded.
        :param str min_last_active_date: Lower bound for a user's last active date, in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). If specified, then only users whose 'lastActiveDate' is not null, and is equal to or later than the given date will be regarded.
        :param str max_last_active_date: Upper bound for a user's last active date, in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). If specified, then only users whose 'lastActiveDate' is null, or is equal to or earlier than the given date will be regarded.
        :param bool include_monthly_stats: Whether to include the 'monthlyStats' for the returned users. If not specified, then the field defaults to 'false'.
        :param str monthly_stats_start_date: Minimum bound for the monthly stats (=oldest month that should be included). Must be passed in the format 'YYYY-MM'. If not specified, then the monthly stats will go back up to the first month in which the user existed (date of the user's registration). Note that this field is only regarded if 'includeMonthlyStats' = true.
        :param str monthly_stats_end_date: Maximum bound for the monthly stats (=latest month that should be included). Must be passed in the format 'YYYY-MM'. If not specified, then the monthly stats will go up to either the current month (for active users), or up to the month of deletion (for deleted users). Note that this field is only regarded if  'includeMonthlyStats' = true.
        :param bool is_deleted: If NOT specified, then the service will regard both active and deleted users in the search. If set to 'true', then ONLY deleted users will be regarded. If set to 'false', then ONLY active users will be regarded.
        :param int page: Result page that you want to retrieve
        :param int per_page: Maximum number of records per page. Can be at most 500. NOTE: Due to its validation and visualization, the swagger frontend might show very low performance, or even crashes, when a service responds with a lot of data. It is recommended to use a HTTP client like Postman or DHC instead of our swagger frontend for service calls with large page sizes.
        :param list[str] order: Determines the order of the results. You can order the results by 'userId'. The default order for this service is 'userId,asc'. The general format is: 'property[,asc|desc]', with 'asc' being the default value. 
        :return: PageableUserInfoList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['min_registration_date', 'max_registration_date', 'min_deletion_date', 'max_deletion_date', 'min_last_active_date', 'max_last_active_date', 'include_monthly_stats', 'monthly_stats_start_date', 'monthly_stats_end_date', 'is_deleted', 'page', 'per_page', 'order']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_user_list" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page' in params and params['page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `get_user_list`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'per_page' in params and params['per_page'] > 500:  # noqa: E501
            raise ValueError("Invalid value for parameter `per_page` when calling `get_user_list`, must be a value less than or equal to `500`")  # noqa: E501
        if 'per_page' in params and params['per_page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `per_page` when calling `get_user_list`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'min_registration_date' in params:
            query_params.append(('minRegistrationDate', params['min_registration_date']))  # noqa: E501
        if 'max_registration_date' in params:
            query_params.append(('maxRegistrationDate', params['max_registration_date']))  # noqa: E501
        if 'min_deletion_date' in params:
            query_params.append(('minDeletionDate', params['min_deletion_date']))  # noqa: E501
        if 'max_deletion_date' in params:
            query_params.append(('maxDeletionDate', params['max_deletion_date']))  # noqa: E501
        if 'min_last_active_date' in params:
            query_params.append(('minLastActiveDate', params['min_last_active_date']))  # noqa: E501
        if 'max_last_active_date' in params:
            query_params.append(('maxLastActiveDate', params['max_last_active_date']))  # noqa: E501
        if 'include_monthly_stats' in params:
            query_params.append(('includeMonthlyStats', params['include_monthly_stats']))  # noqa: E501
        if 'monthly_stats_start_date' in params:
            query_params.append(('monthlyStatsStartDate', params['monthly_stats_start_date']))  # noqa: E501
        if 'monthly_stats_end_date' in params:
            query_params.append(('monthlyStatsEndDate', params['monthly_stats_end_date']))  # noqa: E501
        if 'is_deleted' in params:
            query_params.append(('isDeleted', params['is_deleted']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'per_page' in params:
            query_params.append(('perPage', params['per_page']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
            collection_formats['order'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['finapi_auth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/mandatorAdmin/getUserList', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PageableUserInfoList',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)