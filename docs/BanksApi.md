# swagger_client.BanksApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_and_search_all_banks**](BanksApi.md#get_and_search_all_banks) | **GET** /api/v1/banks | Get and search all banks
[**get_bank**](BanksApi.md#get_bank) | **GET** /api/v1/banks/{id} | Get a bank
[**get_multiple_banks**](BanksApi.md#get_multiple_banks) | **GET** /api/v1/banks/{ids} | Get multiple banks


# **get_and_search_all_banks**
> PageableBankList get_and_search_all_banks(ids=ids, search=search, is_supported=is_supported, pins_are_volatile=pins_are_volatile, supported_data_sources=supported_data_sources, location=location, is_test_bank=is_test_bank, page=page, per_page=per_page, order=order)

Get and search all banks

Get and search banks from finAPI's database of banks. Must pass the authorized user's access_token, or your client's access_token. You can set optional search criteria to get only those banks that you are interested in. If you do not specify any search criteria, then this service functions as a 'get all' service.

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
api_instance = swagger_client.BanksApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | A comma-separated list of bank identifiers. If specified, then only banks whose identifier match any of the given identifiers will be regarded. The maximum number of identifiers is 1000. (optional)
search = 'search_example' # str | If specified, then only those banks will be contained in the result whose 'name', 'blz', 'bic' or 'city' contains the given search string (the matching works case-insensitive). If no banks contain the search string in any of the regarded fields, then the result will be an empty list. Note that you may also pass an IBAN in this field, in which case finAPI will try to find the related bank in its database and regard only this bank for the search. Also note: If the given search string consists of several terms (separated by whitespace), then ALL of these terms must apply to a bank in order for it to get included into the result. (optional)
is_supported = true # bool | If specified, then only supported (in case of 'true' value) or unsupported (in case of 'false' value) banks will be regarded. (optional)
pins_are_volatile = true # bool | If specified, then only those banks will be regarded that have the given value (true or false) for their 'pinsAreVolatile' field. (optional)
supported_data_sources = ['supported_data_sources_example'] # list[str] | Comma-separated list of data sources. Possible values: WEB_SCRAPER,FINTS_SERVER. If this parameter is specified, then only those banks will be regarded in the search that support ALL of the given data sources. Note that this does NOT imply that those data sources must be the only data sources that are supported by a bank. (optional)
location = ['location_example'] # list[str] | Comma-separated list of two-letter country codes (ISO 3166 ALPHA-2). If set, then only those banks will be regarded in the search that are located in the specified countries. Notes: Banks which do not have a location set (i.e. international institutes) will ALWAYS be regarded in the search, independent of what you specify for this field. When you pass a country code that doesn't exist in the ISO 3166 ALPHA-2 standard, then the service will respond with 400 BAD_REQUEST. (optional)
is_test_bank = true # bool | If specified, then only those banks will be regarded that have the given value (true or false) for their 'isTestBank' field. (optional)
page = 1 # int | Result page that you want to retrieve. (optional) (default to 1)
per_page = 20 # int | Maximum number of records per page. Can be at most 500. NOTE: Due to its validation and visualization, the swagger frontend might show very low performance, or even crashes, when a service responds with a lot of data. It is recommended to use a HTTP client like Postman or DHC instead of our swagger frontend for service calls with large page sizes. (optional) (default to 20)
order = ['order_example'] # list[str] | Determines the order of the results. You can order the results by 'id', 'name', 'blz', 'bic' or 'popularity'. The default order for all services is 'id,asc'. You can also order by multiple properties. In that case the order of the parameters passed is important. Example: '/banks?order=name,desc&order=id,asc' will return banks ordered by 'name' (descending), where banks with the same 'name' are ordered by 'id' (ascending). The general format is: 'property[,asc|desc]', with 'asc' being the default value. Please note that ordering by multiple fields is not supported in our swagger frontend, but you can test this feature with any HTTP tool of your choice (e.g. postman or DHC).  (optional)

try:
    # Get and search all banks
    api_response = api_instance.get_and_search_all_banks(ids=ids, search=search, is_supported=is_supported, pins_are_volatile=pins_are_volatile, supported_data_sources=supported_data_sources, location=location, is_test_bank=is_test_bank, page=page, per_page=per_page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BanksApi->get_and_search_all_banks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| A comma-separated list of bank identifiers. If specified, then only banks whose identifier match any of the given identifiers will be regarded. The maximum number of identifiers is 1000. | [optional] 
 **search** | **str**| If specified, then only those banks will be contained in the result whose &#39;name&#39;, &#39;blz&#39;, &#39;bic&#39; or &#39;city&#39; contains the given search string (the matching works case-insensitive). If no banks contain the search string in any of the regarded fields, then the result will be an empty list. Note that you may also pass an IBAN in this field, in which case finAPI will try to find the related bank in its database and regard only this bank for the search. Also note: If the given search string consists of several terms (separated by whitespace), then ALL of these terms must apply to a bank in order for it to get included into the result. | [optional] 
 **is_supported** | **bool**| If specified, then only supported (in case of &#39;true&#39; value) or unsupported (in case of &#39;false&#39; value) banks will be regarded. | [optional] 
 **pins_are_volatile** | **bool**| If specified, then only those banks will be regarded that have the given value (true or false) for their &#39;pinsAreVolatile&#39; field. | [optional] 
 **supported_data_sources** | [**list[str]**](str.md)| Comma-separated list of data sources. Possible values: WEB_SCRAPER,FINTS_SERVER. If this parameter is specified, then only those banks will be regarded in the search that support ALL of the given data sources. Note that this does NOT imply that those data sources must be the only data sources that are supported by a bank. | [optional] 
 **location** | [**list[str]**](str.md)| Comma-separated list of two-letter country codes (ISO 3166 ALPHA-2). If set, then only those banks will be regarded in the search that are located in the specified countries. Notes: Banks which do not have a location set (i.e. international institutes) will ALWAYS be regarded in the search, independent of what you specify for this field. When you pass a country code that doesn&#39;t exist in the ISO 3166 ALPHA-2 standard, then the service will respond with 400 BAD_REQUEST. | [optional] 
 **is_test_bank** | **bool**| If specified, then only those banks will be regarded that have the given value (true or false) for their &#39;isTestBank&#39; field. | [optional] 
 **page** | **int**| Result page that you want to retrieve. | [optional] [default to 1]
 **per_page** | **int**| Maximum number of records per page. Can be at most 500. NOTE: Due to its validation and visualization, the swagger frontend might show very low performance, or even crashes, when a service responds with a lot of data. It is recommended to use a HTTP client like Postman or DHC instead of our swagger frontend for service calls with large page sizes. | [optional] [default to 20]
 **order** | [**list[str]**](str.md)| Determines the order of the results. You can order the results by &#39;id&#39;, &#39;name&#39;, &#39;blz&#39;, &#39;bic&#39; or &#39;popularity&#39;. The default order for all services is &#39;id,asc&#39;. You can also order by multiple properties. In that case the order of the parameters passed is important. Example: &#39;/banks?order&#x3D;name,desc&amp;order&#x3D;id,asc&#39; will return banks ordered by &#39;name&#39; (descending), where banks with the same &#39;name&#39; are ordered by &#39;id&#39; (ascending). The general format is: &#39;property[,asc|desc]&#39;, with &#39;asc&#39; being the default value. Please note that ordering by multiple fields is not supported in our swagger frontend, but you can test this feature with any HTTP tool of your choice (e.g. postman or DHC).  | [optional] 

### Return type

[**PageableBankList**](PageableBankList.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank**
> Bank get_bank(id)

Get a bank

Get a single bank from finAPI's database of banks. You have to pass the bank's identifier, and either the authorized user's access_token, or your client's access token.

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
api_instance = swagger_client.BanksApi(swagger_client.ApiClient(configuration))
id = 789 # int | Identifier of requested bank

try:
    # Get a bank
    api_response = api_instance.get_bank(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BanksApi->get_bank: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identifier of requested bank | 

### Return type

[**Bank**](Bank.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multiple_banks**
> BankList get_multiple_banks(ids)

Get multiple banks

Get a list of multiple banks from finAPI's database of banks. You have to pass a list of bank identifiers, and either the authorized user's access_token, or your client's access token. Note that banks whose identifiers do not exist will not be contained in the result (If this applies to all of the given identifiers, then the result will be an empty list).<br/><br/><b>WARNING</b>: This service is deprecated and will be removed at some point. If you want to get multiple banks, please instead use the service 'Get and search all banks' and pass a comma-separated list of identifiers with the parameter 'ids'.

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
api_instance = swagger_client.BanksApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | Comma-separated list of identifiers of requested banks

try:
    # Get multiple banks
    api_response = api_instance.get_multiple_banks(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BanksApi->get_multiple_banks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| Comma-separated list of identifiers of requested banks | 

### Return type

[**BankList**](BankList.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

