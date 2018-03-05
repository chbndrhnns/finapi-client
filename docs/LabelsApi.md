# swagger_client.LabelsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_label**](LabelsApi.md#create_label) | **POST** /api/v1/labels | Create a new label
[**delete_all_labels**](LabelsApi.md#delete_all_labels) | **DELETE** /api/v1/labels | Delete all labels
[**delete_label**](LabelsApi.md#delete_label) | **DELETE** /api/v1/labels/{id} | Delete a label
[**edit_label**](LabelsApi.md#edit_label) | **PATCH** /api/v1/labels/{id} | Edit a label
[**get_and_search_all_labels**](LabelsApi.md#get_and_search_all_labels) | **GET** /api/v1/labels | Get and search all labels
[**get_label**](LabelsApi.md#get_label) | **GET** /api/v1/labels/{id} | Get a label
[**get_multiple_labels**](LabelsApi.md#get_multiple_labels) | **GET** /api/v1/labels/{ids} | Get multiple labels


# **create_label**
> Label create_label(body)

Create a new label

Create a new label for a specific user. Must pass the new label's name and the user's access_token.<br/><br/>Users can create labels to flag transactions (see method PATCH /transactions), with the goal of collecting and getting an overview of all transactions of a certain 'type'. In this sense, labels are similar to transaction categories. However, labels are supposed to depict more of an implicit meaning of a transaction. For instance, a user might want to assign a flag to a transaction that reminds him that he can offset it against tax. At the same time, the category of the transactions might be something like 'insurance', which is a more 'fact-based', or 'objective' way of typing the transaction. Despite this semantic difference between categories and labels, there is also the difference that a transaction can be assigned multiple labels at the same time (while in contrast it can have just a single category).

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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
body = swagger_client.LabelParams() # LabelParams | Label's name

try:
    # Create a new label
    api_response = api_instance.create_label(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->create_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LabelParams**](LabelParams.md)| Label&#39;s name | 

### Return type

[**Label**](Label.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_labels**
> IdentifierList delete_all_labels()

Delete all labels

Delete all labels of the user that is authorized by the access_token. Must pass the user's access_token.

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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))

try:
    # Delete all labels
    api_response = api_instance.delete_all_labels()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->delete_all_labels: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**IdentifierList**](IdentifierList.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_label**
> delete_label(id)

Delete a label

Delete a single label of the user that is authorized by the access_token. Must pass the label's identifier and the user's access_token.

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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Identifier of the label to delete

try:
    # Delete a label
    api_instance.delete_label(id)
except ApiException as e:
    print("Exception when calling LabelsApi->delete_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identifier of the label to delete | 

### Return type

void (empty response body)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_label**
> Label edit_label(id, body)

Edit a label

Change the name of a label of the user that is authorized by the access_token. Must pass the label's identifier, the label's new name and the user's access_token.

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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Label's identifier
body = swagger_client.LabelParams() # LabelParams | Label's new name

try:
    # Edit a label
    api_response = api_instance.edit_label(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->edit_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Label&#39;s identifier | 
 **body** | [**LabelParams**](LabelParams.md)| Label&#39;s new name | 

### Return type

[**Label**](Label.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_and_search_all_labels**
> PageableLabelList get_and_search_all_labels(ids=ids, search=search, page=page, per_page=per_page, order=order)

Get and search all labels

Get labels of the user that is authorized by the access_token. Must pass the user's access_token. You can set optional search criteria to get only those labels that you are interested in. If you do not specify any search criteria, then this service functions as a 'get all' service.

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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | A comma-separated list of label identifiers. If specified, then only labels whose identifier match any of the given identifiers will be regarded. The maximum number of identifiers is 1000. (optional)
search = 'search_example' # str | If specified, then only those labels will be contained in the result whose 'name' contains the given search string (the matching works case-insensitive). If no labels contain the search string in their name, then the result will be an empty list. NOTE: If the given search string consists of several terms (separated by whitespace), then ALL of these terms must be contained in the name in order for a label to get included into the result. (optional)
page = 1 # int | Result page that you want to retrieve (optional) (default to 1)
per_page = 20 # int | Maximum number of records per page. Can be at most 500. NOTE: Due to its validation and visualization, the swagger frontend might show very low performance, or even crashes, when a service responds with a lot of data. It is recommended to use a HTTP client like Postman or DHC instead of our swagger frontend for service calls with large page sizes. (optional) (default to 20)
order = ['order_example'] # list[str] | Determines the order of the results. You can order the results by 'id' or 'name'. The default order for all services is 'id,asc'. Since both fields (id and name) are unique, ordering by multiple fields is pointless. The general format is: 'property[,asc|desc]', with 'asc' being the default value.  (optional)

try:
    # Get and search all labels
    api_response = api_instance.get_and_search_all_labels(ids=ids, search=search, page=page, per_page=per_page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->get_and_search_all_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| A comma-separated list of label identifiers. If specified, then only labels whose identifier match any of the given identifiers will be regarded. The maximum number of identifiers is 1000. | [optional] 
 **search** | **str**| If specified, then only those labels will be contained in the result whose &#39;name&#39; contains the given search string (the matching works case-insensitive). If no labels contain the search string in their name, then the result will be an empty list. NOTE: If the given search string consists of several terms (separated by whitespace), then ALL of these terms must be contained in the name in order for a label to get included into the result. | [optional] 
 **page** | **int**| Result page that you want to retrieve | [optional] [default to 1]
 **per_page** | **int**| Maximum number of records per page. Can be at most 500. NOTE: Due to its validation and visualization, the swagger frontend might show very low performance, or even crashes, when a service responds with a lot of data. It is recommended to use a HTTP client like Postman or DHC instead of our swagger frontend for service calls with large page sizes. | [optional] [default to 20]
 **order** | [**list[str]**](str.md)| Determines the order of the results. You can order the results by &#39;id&#39; or &#39;name&#39;. The default order for all services is &#39;id,asc&#39;. Since both fields (id and name) are unique, ordering by multiple fields is pointless. The general format is: &#39;property[,asc|desc]&#39;, with &#39;asc&#39; being the default value.  | [optional] 

### Return type

[**PageableLabelList**](PageableLabelList.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_label**
> Label get_label(id)

Get a label

Get a single label of the user that is authorized by the access_token. Must pass the label's identifier and the user's access_token.

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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Identifier of requested label

try:
    # Get a label
    api_response = api_instance.get_label(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->get_label: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identifier of requested label | 

### Return type

[**Label**](Label.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multiple_labels**
> LabelList get_multiple_labels(ids)

Get multiple labels

Get a list of multiple labels of the user that is authorized by the access_token.Must pass the labels' identifiers and the user's access_token. Identifiers that do not exist or do not relate to the authorized user will not be contained in the result (If this applies to all of the given identifiers, then the result will be an empty list). WARNING: This service is deprecated and will be removed at some point. If you want to get multiple labels, please instead use the service 'Get all labels' and pass a comma-separated list of identifiers as a parameter 'ids'.

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
api_instance = swagger_client.LabelsApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | Comma-separated list of identifiers of requested labels

try:
    # Get multiple labels
    api_response = api_instance.get_multiple_labels(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LabelsApi->get_multiple_labels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| Comma-separated list of identifiers of requested labels | 

### Return type

[**LabelList**](LabelList.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

