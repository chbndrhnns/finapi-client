# swagger_client.UsersApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UsersApi.md#create_user) | **POST** /api/v1/users | Create a new user
[**delete_authorized_user**](UsersApi.md#delete_authorized_user) | **DELETE** /api/v1/users | Delete the authorized user
[**delete_unverified_user**](UsersApi.md#delete_unverified_user) | **DELETE** /api/v1/users/{userId} | Delete an unverified user
[**edit_authorized_user**](UsersApi.md#edit_authorized_user) | **PATCH** /api/v1/users | Edit the authorized user
[**execute_password_change**](UsersApi.md#execute_password_change) | **POST** /api/v1/users/executePasswordChange | Execute password change
[**get_authorized_user**](UsersApi.md#get_authorized_user) | **GET** /api/v1/users | Get the authorized user
[**get_verification_status**](UsersApi.md#get_verification_status) | **GET** /api/v1/users/verificationStatus | Get a user&#39;s verification status
[**request_password_change**](UsersApi.md#request_password_change) | **POST** /api/v1/users/requestPasswordChange | Request password change
[**verify_user**](UsersApi.md#verify_user) | **POST** /api/v1/users/verify/{userId} | Verify a user


# **create_user**
> User create_user(body)

Create a new user

<p>Create a new user. Must pass your global (i.e. client) access_token. </p><p>This service returns the user's password as plain text. The automatic update of the user's bank connections is disabled by default for any new user. User identifiers are regarded case-insensitive by finAPI.</p><p>Please note that finAPI generally has a restricted set of allowed characters for input fields. You can find the allowed characters <a href = \"https://finapi.zendesk.com/hc/en-us/articles/222013148-What-symbols-are-allowed-in-finAPI-\">here</a>. If a field does not explicitly specify a set of allowed characters, then these are the characters that are allowed for the field. Some fields may specify a different set of characters, in which case this will be documented for the field (like for the 'id' field in this service).</p>

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserCreateParamsImpl() # UserCreateParamsImpl | User's details

try:
    # Create a new user
    api_response = api_instance.create_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserCreateParamsImpl**](UserCreateParamsImpl.md)| User&#39;s details | 

### Return type

[**User**](User.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authorized_user**
> delete_authorized_user()

Delete the authorized user

Delete the authorized user. Must pass the user's access_token. ATTENTION: This deletes the user including all of his bank connections, accounts, balance data and transactions! THIS PROCESS CANNOT BE UNDONE! Note that a user cannot get deleted while any of his bank connections are currently busy (in the process of import, update, or transactions categorization). <p>Note: finAPI will send a notification about the deletion of the user to each of your clients that has a user synchronization callback URL set in its configuration. This also includes the client that is performing this request.</p>

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # Delete the authorized user
    api_instance.delete_authorized_user()
except ApiException as e:
    print("Exception when calling UsersApi->delete_authorized_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_unverified_user**
> delete_unverified_user(user_id)

Delete an unverified user

Delete an unverified user. Must pass your global (i.e. client) access_token.<p>Note: finAPI will send a notification about the deletion of the user to each of your clients that has a user synchronization callback URL set in its configuration. This also includes the client that is performing this request.</p>Also note that finAPI regards user identifiers case-insensitive.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | 

try:
    # Delete an unverified user
    api_instance.delete_unverified_user(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->delete_unverified_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_authorized_user**
> User edit_authorized_user(body)

Edit the authorized user

Edit the authorized user's data and settings. Must pass the user's access_token. Pass an empty string (but not null) to unset either the email or phone number. At least one field must have a non-null value in the request body. This service returns the user's password in distorted form.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.UserUpdateParamsImpl() # UserUpdateParamsImpl | User's details

try:
    # Edit the authorized user
    api_response = api_instance.edit_authorized_user(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->edit_authorized_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserUpdateParamsImpl**](UserUpdateParamsImpl.md)| User&#39;s details | 

### Return type

[**User**](User.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_password_change**
> execute_password_change(body=body)

Execute password change

Change the password of a user. Must pass your global (i.e. client) access_token.<br/><br/>Note: When changing the password of a user, all tokens that have been handed out for that user (for whatever client) will be revoked! Also note that finAPI regards user identifiers case-insensitive.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.ExecutePasswordChangeParams() # ExecutePasswordChangeParams |  (optional)

try:
    # Execute password change
    api_instance.execute_password_change(body=body)
except ApiException as e:
    print("Exception when calling UsersApi->execute_password_change: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExecutePasswordChangeParams**](ExecutePasswordChangeParams.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorized_user**
> User get_authorized_user()

Get the authorized user

Get the authorized user's data. Must pass the user's access_token. Only the authorized user can get his data, i.e. his access_token must be used. Note that each symbol of the password is distorted with an 'X' character, i.e. if the user's password is '123456', the service will return the string 'XXXXXX'.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))

try:
    # Get the authorized user
    api_response = api_instance.get_authorized_user()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_authorized_user: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_verification_status**
> VerificationStatusResource get_verification_status(user_id)

Get a user's verification status

Get the verification status of the requested user. Must pass your global (i.e. client) access_token. Note that finAPI regards user identifiers case-insensitive.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | User's identifier

try:
    # Get a user's verification status
    api_response = api_instance.get_verification_status(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_verification_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s identifier | 

### Return type

[**VerificationStatusResource**](VerificationStatusResource.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_password_change**
> PasswordChangingResource request_password_change(body=body)

Request password change

Request password change for a user. Must pass your global (i.e. client) access_token. Note that finAPI regards user identifiers case-insensitive.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
body = swagger_client.RequestPasswordChangeParameters() # RequestPasswordChangeParameters |  (optional)

try:
    # Request password change
    api_response = api_instance.request_password_change(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->request_password_change: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestPasswordChangeParameters**](RequestPasswordChangeParameters.md)|  | [optional] 

### Return type

[**PasswordChangingResource**](PasswordChangingResource.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_user**
> verify_user(user_id)

Verify a user

Verify a user. Must pass your global (i.e. client) access_token. Note that finAPI regards user identifiers case-insensitive.

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
api_instance = swagger_client.UsersApi(swagger_client.ApiClient(configuration))
user_id = 'user_id_example' # str | User's identifier

try:
    # Verify a user
    api_instance.verify_user(user_id)
except ApiException as e:
    print("Exception when calling UsersApi->verify_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| User&#39;s identifier | 

### Return type

void (empty response body)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

