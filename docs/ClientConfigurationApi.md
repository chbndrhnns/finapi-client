# swagger_client.ClientConfigurationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**edit_client_configuration**](ClientConfigurationApi.md#edit_client_configuration) | **PATCH** /api/v1/clientConfiguration | Edit client configuration
[**get_client_configuration**](ClientConfigurationApi.md#get_client_configuration) | **GET** /api/v1/clientConfiguration | Get client configuration


# **edit_client_configuration**
> ClientConfiguration edit_client_configuration(body=body)

Edit client configuration

Edit your client's configuration. Must pass your global (i.e. client) access_token.<br/><br/> <b>NOTE</b>: When token validity periods are changed, this only applies to newly requested tokens, and does not change the expiration time of already existing tokens.

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
api_instance = swagger_client.ClientConfigurationApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClientConfigurationParams() # ClientConfigurationParams | Client configuration parameters (optional)

try:
    # Edit client configuration
    api_response = api_instance.edit_client_configuration(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientConfigurationApi->edit_client_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientConfigurationParams**](ClientConfigurationParams.md)| Client configuration parameters | [optional] 

### Return type

[**ClientConfiguration**](ClientConfiguration.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_configuration**
> ClientConfiguration get_client_configuration()

Get client configuration

Get your client's configuration. Must pass your global (i.e. client) access_token.

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
api_instance = swagger_client.ClientConfigurationApi(swagger_client.ApiClient(configuration))

try:
    # Get client configuration
    api_response = api_instance.get_client_configuration()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientConfigurationApi->get_client_configuration: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ClientConfiguration**](ClientConfiguration.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

