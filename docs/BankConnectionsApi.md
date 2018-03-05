# swagger_client.BankConnectionsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_all_bank_connections**](BankConnectionsApi.md#delete_all_bank_connections) | **DELETE** /api/v1/bankConnections | Delete all bank connections
[**delete_bank_connection**](BankConnectionsApi.md#delete_bank_connection) | **DELETE** /api/v1/bankConnections/{id} | Delete a bank connection
[**edit_bank_connection**](BankConnectionsApi.md#edit_bank_connection) | **PATCH** /api/v1/bankConnections/{id} | Edit a bank connection
[**get_all_bank_connections**](BankConnectionsApi.md#get_all_bank_connections) | **GET** /api/v1/bankConnections | Get all bank connections
[**get_bank_connection**](BankConnectionsApi.md#get_bank_connection) | **GET** /api/v1/bankConnections/{id} | Get a bank connection
[**get_multiple_bank_connections**](BankConnectionsApi.md#get_multiple_bank_connections) | **GET** /api/v1/bankConnections/{ids} | Get multiple bank connections
[**import_bank_connection**](BankConnectionsApi.md#import_bank_connection) | **POST** /api/v1/bankConnections/import | Import a new bank connection
[**update_bank_connection**](BankConnectionsApi.md#update_bank_connection) | **POST** /api/v1/bankConnections/update | Update a bank connection


# **delete_all_bank_connections**
> IdentifierList delete_all_bank_connections()

Delete all bank connections

Delete all bank connections of the user that is authorized by the access_token. Must pass the user's access_token.<br/><br/>Notes: <br/>- All notification rules that are connected to any specific bank connection will get deleted as well. <br/>- If at least one bank connection is busy (currently in the process of import, update, or transactions categorization), then this service will perform no action at all.

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
api_instance = swagger_client.BankConnectionsApi(swagger_client.ApiClient(configuration))

try:
    # Delete all bank connections
    api_response = api_instance.delete_all_bank_connections()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankConnectionsApi->delete_all_bank_connections: %s\n" % e)
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

# **delete_bank_connection**
> delete_bank_connection(id)

Delete a bank connection

Delete a single bank connection of the user that is authorized by the access_token, including all of its accounts and their transactions and balance data. Must pass the connection's identifier and the user's access_token.<br/><br/>Notes: <br/>- All notification rules that are connected to the bank connection will get adjusted so that they no longer have this connection listed. Notification rules that are connected to just this bank connection (and no other connection) will get deleted altogether. <br/>- A bank connection cannot get deleted while it is in the process of import, update, or transactions categorization.

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
api_instance = swagger_client.BankConnectionsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Identifier of the bank connection to delete

try:
    # Delete a bank connection
    api_instance.delete_bank_connection(id)
except ApiException as e:
    print("Exception when calling BankConnectionsApi->delete_bank_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identifier of the bank connection to delete | 

### Return type

void (empty response body)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_bank_connection**
> BankConnection edit_bank_connection(id, body)

Edit a bank connection

Change the stored authentication credentials (banking user ID, banking customer ID, and banking PIN), or other fields of the bank connection. Must pass the connection's identifier and the user's access_token.<br/><br/>Note that a bank connection's credentials cannot be changed while it is in the process of import, update, or transactions categorization.

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
api_instance = swagger_client.BankConnectionsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Identifier of the bank connection to change the parameters for
body = swagger_client.EditBankConnectionParams() # EditBankConnectionParams | New bank connection parameters

try:
    # Edit a bank connection
    api_response = api_instance.edit_bank_connection(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankConnectionsApi->edit_bank_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identifier of the bank connection to change the parameters for | 
 **body** | [**EditBankConnectionParams**](EditBankConnectionParams.md)| New bank connection parameters | 

### Return type

[**BankConnection**](BankConnection.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_bank_connections**
> BankConnectionList get_all_bank_connections(ids=ids)

Get all bank connections

Get bank connections of the user that is authorized by the access_token. Must pass the user's access_token. You can set optional search criteria to get only those bank connections that you are interested in. If you do not specify any search criteria, then this service functions as a 'get all' service.

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
api_instance = swagger_client.BankConnectionsApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | A comma-separated list of bank connection identifiers. If specified, then only bank connections whose identifier match any of the given identifiers will be regarded. The maximum number of identifiers is 1000. (optional)

try:
    # Get all bank connections
    api_response = api_instance.get_all_bank_connections(ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankConnectionsApi->get_all_bank_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| A comma-separated list of bank connection identifiers. If specified, then only bank connections whose identifier match any of the given identifiers will be regarded. The maximum number of identifiers is 1000. | [optional] 

### Return type

[**BankConnectionList**](BankConnectionList.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bank_connection**
> BankConnection get_bank_connection(id)

Get a bank connection

Get a single bank connection of the user that is authorized by the access_token. Must pass the connection's identifier and the user's access_token.

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
api_instance = swagger_client.BankConnectionsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Identifier of requested bank connection

try:
    # Get a bank connection
    api_response = api_instance.get_bank_connection(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankConnectionsApi->get_bank_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identifier of requested bank connection | 

### Return type

[**BankConnection**](BankConnection.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multiple_bank_connections**
> BankConnectionList get_multiple_bank_connections(ids)

Get multiple bank connections

Get a list of multiple bank connections of the user that is authorized by the access_token. Must pass the connections' identifiers and the user's access_token. Connections whose identifiers do not exist or do not relate to the authorized user will not be contained in the result (If this applies to all of the given identifiers, then the result will be an empty list). WARNING: This service is deprecated and will be removed at some point. If you want to get multiple bank connections, please instead use the service 'Get all bank connections' and pass a comma-separated list of identifiers as a parameter 'ids'.

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
api_instance = swagger_client.BankConnectionsApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | Comma-separated list of identifiers of requested bank connections

try:
    # Get multiple bank connections
    api_response = api_instance.get_multiple_bank_connections(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankConnectionsApi->get_multiple_bank_connections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| Comma-separated list of identifiers of requested bank connections | 

### Return type

[**BankConnectionList**](BankConnectionList.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_bank_connection**
> BankConnection import_bank_connection(body)

Import a new bank connection

Imports a new bank connection for a specific user. Must pass the connection credentials and the user's access_token. All bank accounts will be downloaded and imported with their current balances, transactions and supported two-step procedures (note that the amount of available transactions may vary between banks, e.g. some banks deliver all transactions from the past year, others only deliver the transactions from the past three months). The balance and transactions download process runs asynchronously, so this service may return before all balances and transactions have been imported. Also, all downloaded transactions will be categorized by a separate background process that runs asynchronously too. To check the status of the balance and transactions download process as well as the background categorization process, see the status flags that are returned by the GET /bankConnections/<id> service.<br/><br/>Note that some banks may require a multi-step authentication, in which case the service will respond with HTTP code 510 and an error message containing a challenge for the user from the bank. You must display the challenge message to the user, and then retry the service call, passing the user's answer to the bank's challenge in the 'challengeResponse' field.<br/><br/>You can also import a \"demo connection\" which contains a single bank account with some pre-defined transactions. To import the demo connection, you need to pass the identifier of the \"demo bank\", which is a bank with BLZ 00000000 (see GET /banks/search). In case of demo connection import, any other fields besides the demo bank identifier can remain unset. The bankingUserId, bankingPin, and storePin fields will be stored, however they will generally not be relevant when updating the bank connection. Also, the skipPositionsDownload flag is ignored for the demo bank connection, i.e. when importing the demo bank connection, you will always get the transactions for its account. You can enable multi-step authentication for the demo bank connection by setting the bank connection name to \"MSA\".<br/><br/>For a more in-depth understanding of the import process, please also read this article on our Dev Portal: <a href='https://finapi.zendesk.com/hc/en-us/articles/115000296607-Import-Update-of-Bank-Connections-Accounts'>Import & Update of Bank Connections / Accounts</a>

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
api_instance = swagger_client.BankConnectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ImportBankConnectionParams() # ImportBankConnectionParams | Import bank connection parameters

try:
    # Import a new bank connection
    api_response = api_instance.import_bank_connection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankConnectionsApi->import_bank_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ImportBankConnectionParams**](ImportBankConnectionParams.md)| Import bank connection parameters | 

### Return type

[**BankConnection**](BankConnection.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bank_connection**
> BankConnection update_bank_connection(body)

Update a bank connection

Update an existing bank connection of the user that is authorized by the access_token. Downloads and imports the current account balances and new transactions. Must pass the connection's identifier and the user's access_token. For more information about the processes of authentication, data download and transactions categorization, see POST /bankConnections/import. Note that supported two-step procedures are updated as well. It may unset the current default two-step procedure of the given bank connection (but only if this procedure is not supported anymore by the bank). You can also update the \"demo connection\" (in this case, the fields 'bankingPin', 'importNewAccounts', and 'skipPositionsDownload' will be ignored).<br/><br/>Note that you cannot trigger an update of a bank connection as long as there is still a previously triggered update running.<br/><br/>For a more in-depth understanding of the update process, please also read this article on our Dev Portal: <a href='https://finapi.zendesk.com/hc/en-us/articles/115000296607-Import-Update-of-Bank-Connections-Accounts'>Import & Update of Bank Connections / Accounts</a>

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
api_instance = swagger_client.BankConnectionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateBankConnectionParams() # UpdateBankConnectionParams | Update bank connection parameters

try:
    # Update a bank connection
    api_response = api_instance.update_bank_connection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankConnectionsApi->update_bank_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateBankConnectionParams**](UpdateBankConnectionParams.md)| Update bank connection parameters | 

### Return type

[**BankConnection**](BankConnection.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

