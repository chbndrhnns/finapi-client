# swagger_client.NotificationRulesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_notification_rule**](NotificationRulesApi.md#create_notification_rule) | **POST** /api/v1/notificationRules | Create a new notification rule
[**delete_all_notification_rules**](NotificationRulesApi.md#delete_all_notification_rules) | **DELETE** /api/v1/notificationRules | Delete all notification rules
[**delete_notification_rule**](NotificationRulesApi.md#delete_notification_rule) | **DELETE** /api/v1/notificationRules/{id} | Delete a notification rule
[**get_and_search_all_notification_rules**](NotificationRulesApi.md#get_and_search_all_notification_rules) | **GET** /api/v1/notificationRules | Get and search all notification rules
[**get_notification_rule**](NotificationRulesApi.md#get_notification_rule) | **GET** /api/v1/notificationRules/{id} | Get a notification rule


# **create_notification_rule**
> NotificationRule create_notification_rule(body)

Create a new notification rule

Create a new notification rule for a specific user. Must pass the user's access_token.<br/><br/>Setting up notification rules for a user allows your client application to get notified about changes in the user's data, e.g. when new transactions were downloaded, an account's balance has changed, or the user's banking credentials are no longer correct. Note that currently, this feature is implemented only for finAPI's automatic batch update, i.e. notification rules are only relevant when the user has activated the automatic updates (and when the automatic batch update is activated in general for your client).<br/><br/>There are different kinds of notification rules. The kind of a rule is depicted by the 'triggerEvent'. The trigger event specifies what data you have to pass when creating a rule (specifically, the contents of the 'params' field), on which events finAPI will send notifications to your client application, as well as what data is contained in those notifications. The specifics of the different trigger events are documented in the following article on our Dev Portal: <a href='https://finapi.zendesk.com/hc/en-us/articles/232324608-How-to-create-notification-rules-and-receive-notifications'>How to create notification rules and receive notifications</a>

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
api_instance = swagger_client.NotificationRulesApi(swagger_client.ApiClient(configuration))
body = swagger_client.NotificationRuleParams() # NotificationRuleParams | Notification rule parameters

try:
    # Create a new notification rule
    api_response = api_instance.create_notification_rule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationRulesApi->create_notification_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NotificationRuleParams**](NotificationRuleParams.md)| Notification rule parameters | 

### Return type

[**NotificationRule**](NotificationRule.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_notification_rules**
> IdentifierList delete_all_notification_rules()

Delete all notification rules

Delete all notification rules of the user that is authorized by the access_token. Must pass the user's access_token. 

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
api_instance = swagger_client.NotificationRulesApi(swagger_client.ApiClient(configuration))

try:
    # Delete all notification rules
    api_response = api_instance.delete_all_notification_rules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationRulesApi->delete_all_notification_rules: %s\n" % e)
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

# **delete_notification_rule**
> delete_notification_rule(id)

Delete a notification rule

Delete a single notification rule of the user that is authorized by the access_token. Must pass the notification rule's identifier and the user's access_token.

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
api_instance = swagger_client.NotificationRulesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Identifier of the notification rule to delete

try:
    # Delete a notification rule
    api_instance.delete_notification_rule(id)
except ApiException as e:
    print("Exception when calling NotificationRulesApi->delete_notification_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identifier of the notification rule to delete | 

### Return type

void (empty response body)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_and_search_all_notification_rules**
> NotificationRuleList get_and_search_all_notification_rules(ids=ids, trigger_event=trigger_event, include_details=include_details)

Get and search all notification rules

Get notification rules of the user that is authorized by the access_token. Must pass the user's access_token. You can set optional search criteria to get only those notification rules that you are interested in. If you do not specify any search criteria, then this service functions as a 'get all' service.

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
api_instance = swagger_client.NotificationRulesApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | A comma-separated list of notification rule identifiers. If specified, then only notification rules whose identifier match any of the given identifiers will be regarded. The maximum number of identifiers is 1000. (optional)
trigger_event = 'trigger_event_example' # str | If specified, then only notification rules with given trigger event will be regarded. (optional)
include_details = true # bool | If specified, then only notification rules that include or not include details will be regarded. (optional)

try:
    # Get and search all notification rules
    api_response = api_instance.get_and_search_all_notification_rules(ids=ids, trigger_event=trigger_event, include_details=include_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationRulesApi->get_and_search_all_notification_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| A comma-separated list of notification rule identifiers. If specified, then only notification rules whose identifier match any of the given identifiers will be regarded. The maximum number of identifiers is 1000. | [optional] 
 **trigger_event** | **str**| If specified, then only notification rules with given trigger event will be regarded. | [optional] 
 **include_details** | **bool**| If specified, then only notification rules that include or not include details will be regarded. | [optional] 

### Return type

[**NotificationRuleList**](NotificationRuleList.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_notification_rule**
> NotificationRule get_notification_rule(id)

Get a notification rule

Get a single notification rule of the user that is authorized by the access_token. Must pass the notification rule's identifier and the user's access_token.

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
api_instance = swagger_client.NotificationRulesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Identifier of requested notification rule

try:
    # Get a notification rule
    api_response = api_instance.get_notification_rule(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotificationRulesApi->get_notification_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identifier of requested notification rule | 

### Return type

[**NotificationRule**](NotificationRule.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

