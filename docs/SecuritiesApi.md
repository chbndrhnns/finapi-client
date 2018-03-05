# swagger_client.SecuritiesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_and_search_all_securities**](SecuritiesApi.md#get_and_search_all_securities) | **GET** /api/v1/securities | Get and search all securities
[**get_multiple_securities**](SecuritiesApi.md#get_multiple_securities) | **GET** /api/v1/securities/{ids} | Get multiple securities
[**get_security**](SecuritiesApi.md#get_security) | **GET** /api/v1/securities/{id} | Get a security


# **get_and_search_all_securities**
> PageableSecurityList get_and_search_all_securities(ids=ids, search=search, account_ids=account_ids, page=page, per_page=per_page, order=order)

Get and search all securities

Get securities of the user that is authorized by the access_token. Must pass the user's access_token. You can set optional search criteria to get only those securities that you are interested in. If you do not specify any search criteria, then this service functions as a 'get all' service.<p>Note: Whenever a security account is being updated, its security positions will be internally re-created, meaning that the identifier of a security position might change over time.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: finapi_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SecuritiesApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | A comma-separated list of security identifiers. If specified, then only securities whose identifier match any of the given identifiers will be regarded. The maximum number of identifiers is 1000. (optional)
search = 'search_example' # str | If specified, then only those securities will be contained in the result whose 'name', 'isin' or 'wkn' contains the given search string (the matching works case-insensitive). If no securities contain the search string in any of these fields, then the result will be an empty list. NOTE: If the given search string consists of several terms (separated by whitespace), then ALL of these terms must be contained in the searched fields in order for a security to get included into the result. (optional)
account_ids = [56] # list[int] | Comma-separated list of identifiers of accounts (optional)
page = 1 # int | Result page that you want to retrieve. (optional) (default to 1)
per_page = 20 # int | Maximum number of records per page. Can be at most 500. NOTE: Due to its validation and visualization, the swagger frontend might show very low performance, or even crashes, when a service responds with a lot of data. It is recommended to use a HTTP client like Postman or DHC instead of our swagger frontend for service calls with large page sizes. (optional) (default to 20)
order = ['order_example'] # list[str] | Determines the order of the results. You can order the results by next fields: 'id', 'name', 'isin', 'wkn', 'quote', 'quantityNominal', 'marketValue' and 'entryQuote'. The default order for all services is 'id,asc'. You can also order by multiple properties. In that case the order of the parameters passed is important. The general format is: 'property[,asc|desc]', with 'asc' being the default value. Please note that ordering by multiple fields is not supported in our swagger frontend, but you can test this feature with any HTTP tool of your choice (e.g. postman or DHC).  (optional)

try:
    # Get and search all securities
    api_response = api_instance.get_and_search_all_securities(ids=ids, search=search, account_ids=account_ids, page=page, per_page=per_page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecuritiesApi->get_and_search_all_securities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| A comma-separated list of security identifiers. If specified, then only securities whose identifier match any of the given identifiers will be regarded. The maximum number of identifiers is 1000. | [optional] 
 **search** | **str**| If specified, then only those securities will be contained in the result whose &#39;name&#39;, &#39;isin&#39; or &#39;wkn&#39; contains the given search string (the matching works case-insensitive). If no securities contain the search string in any of these fields, then the result will be an empty list. NOTE: If the given search string consists of several terms (separated by whitespace), then ALL of these terms must be contained in the searched fields in order for a security to get included into the result. | [optional] 
 **account_ids** | [**list[int]**](int.md)| Comma-separated list of identifiers of accounts | [optional] 
 **page** | **int**| Result page that you want to retrieve. | [optional] [default to 1]
 **per_page** | **int**| Maximum number of records per page. Can be at most 500. NOTE: Due to its validation and visualization, the swagger frontend might show very low performance, or even crashes, when a service responds with a lot of data. It is recommended to use a HTTP client like Postman or DHC instead of our swagger frontend for service calls with large page sizes. | [optional] [default to 20]
 **order** | [**list[str]**](str.md)| Determines the order of the results. You can order the results by next fields: &#39;id&#39;, &#39;name&#39;, &#39;isin&#39;, &#39;wkn&#39;, &#39;quote&#39;, &#39;quantityNominal&#39;, &#39;marketValue&#39; and &#39;entryQuote&#39;. The default order for all services is &#39;id,asc&#39;. You can also order by multiple properties. In that case the order of the parameters passed is important. The general format is: &#39;property[,asc|desc]&#39;, with &#39;asc&#39; being the default value. Please note that ordering by multiple fields is not supported in our swagger frontend, but you can test this feature with any HTTP tool of your choice (e.g. postman or DHC).  | [optional] 

### Return type

[**PageableSecurityList**](PageableSecurityList.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multiple_securities**
> SecurityList get_multiple_securities(ids)

Get multiple securities

Get a list of multiple securities of the user that is authorized by the access_token. Must pass the securities' identifiers and the user's access_token. Securities whose identifiers do not exist or do not relate to the authorized user will not be contained in the result (If this applies to all of the given identifiers, then the result will be an empty list). <p>Note: Whenever a security account is being updated, its security positions will be internally re-created, meaning that the identifier of a security position might change over time.</p><p>WARNING: This service is deprecated and will be removed at some point. If you want to get multiple securities, please instead use the service 'Get and search all securities' and pass a comma-separated list of identifiers as a parameter 'ids'.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: finapi_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SecuritiesApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | Comma-separated list of identifiers of requested securities

try:
    # Get multiple securities
    api_response = api_instance.get_multiple_securities(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecuritiesApi->get_multiple_securities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| Comma-separated list of identifiers of requested securities | 

### Return type

[**SecurityList**](SecurityList.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_security**
> Security get_security(id)

Get a security

Get a single security for a specific user. Must pass the security's identifier and the user's access_token. <p>Note: Whenever a security account is being updated, its security positions will be internally re-created, meaning that the identifier of a security position might change over time.</p>

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: finapi_auth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.SecuritiesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Security identifier

try:
    # Get a security
    api_response = api_instance.get_security(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SecuritiesApi->get_security: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Security identifier | 

### Return type

[**Security**](Security.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

