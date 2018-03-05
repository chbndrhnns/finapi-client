# swagger_client.TransactionsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_all_transactions**](TransactionsApi.md#delete_all_transactions) | **DELETE** /api/v1/transactions | Delete all transactions
[**delete_transaction**](TransactionsApi.md#delete_transaction) | **DELETE** /api/v1/transactions/{id} | Delete a transaction
[**edit_multiple_transactions**](TransactionsApi.md#edit_multiple_transactions) | **PATCH** /api/v1/transactions | Edit multiple transactions
[**edit_multiple_transactions_deprecated**](TransactionsApi.md#edit_multiple_transactions_deprecated) | **PATCH** /api/v1/transactions/{ids} | Edit multiple transactions (DEPRECATED)
[**edit_transaction**](TransactionsApi.md#edit_transaction) | **PATCH** /api/v1/transactions/{id} | Edit a transaction
[**get_and_search_all_transactions**](TransactionsApi.md#get_and_search_all_transactions) | **GET** /api/v1/transactions | Get and search all transactions
[**get_multiple_transactions**](TransactionsApi.md#get_multiple_transactions) | **GET** /api/v1/transactions/{ids} | Get multiple transactions
[**get_transaction**](TransactionsApi.md#get_transaction) | **GET** /api/v1/transactions/{id} | Get a transaction
[**restore_transaction**](TransactionsApi.md#restore_transaction) | **POST** /api/v1/transactions/{id}/restore | Restore a transaction
[**split_transaction**](TransactionsApi.md#split_transaction) | **POST** /api/v1/transactions/{id}/split | Split a transaction
[**trigger_categorization**](TransactionsApi.md#trigger_categorization) | **POST** /api/v1/transactions/triggerCategorization | Trigger categorization


# **delete_all_transactions**
> IdentifierList delete_all_transactions()

Delete all transactions

Delete all deletable transactions of the currently authorized user. <br/>A transaction is deletable if at least one of the following holds true:<br/> &bull; The transaction belongs to a demo account <br/> &bull; The transaction's 'potentialDuplicate' flag is set to TRUE<br/> &bull; The transaction is an adjusting entry ('Zwischensaldo' transaction) that was added by finAPI

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))

try:
    # Delete all transactions
    api_response = api_instance.delete_all_transactions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->delete_all_transactions: %s\n" % e)
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

# **delete_transaction**
> delete_transaction(id)

Delete a transaction

Delete a single transaction of the user that is authorized by the access_token.  A transaction can only get deleted if at least one of the following holds true:<br/> &bull; The transaction belongs to a demo account <br/> &bull; The transaction's 'potentialDuplicate' flag is set to TRUE<br/> &bull; The transaction is an adjusting entry ('Zwischensaldo' transaction) that was added by finAPI

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Identifier of transaction

try:
    # Delete a transaction
    api_instance.delete_transaction(id)
except ApiException as e:
    print("Exception when calling TransactionsApi->delete_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identifier of transaction | 

### Return type

void (empty response body)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_multiple_transactions**
> IdentifierList edit_multiple_transactions(body)

Edit multiple transactions

Edit one or multiple transactions. You can edit the following fields: 'isNew=true|false' and/or 'isPotentialDuplicate=false' and/or 'categoryId=<id>' and/or 'labelIds=[<ids>]'. To clear the category of the given transactions (so that they are no longer categorized), pass the value '0' as the categoryId. To clear the labels of the given transactions, pass an empty array of label identifiers: '[]'. The parameters 'categoryId' and 'labelIds' are forbidden if 'ids' is NOT set (i.e. you cannot update the category or labels for ALL transactions). The result is a list of identifiers of only those transactions that have changed as a result of this service call.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateMultipleTransactionsParams() # UpdateMultipleTransactionsParams | Update transactions parameters

try:
    # Edit multiple transactions
    api_response = api_instance.edit_multiple_transactions(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->edit_multiple_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateMultipleTransactionsParams**](UpdateMultipleTransactionsParams.md)| Update transactions parameters | 

### Return type

[**IdentifierList**](IdentifierList.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_multiple_transactions_deprecated**
> IdentifierList edit_multiple_transactions_deprecated(ids, body)

Edit multiple transactions (DEPRECATED)

Change the fields of multiple transactions. You can change the following fields: 'isNew=true|false' and/or 'isPotentialDuplicate=false' and/or 'categoryId=<id>' and/or 'labelIds=[<ids>]'. The max number of input identifiers is limited to 100. To clear the category of the given transactions (so that they are no longer categorized), pass the value '0' as the categoryId. To clear the labels of the given transactions, pass an empty array of label identifiers: '[]'. The result is a list of identifiers of only those transactions that have changed as a result of this service call. WARNING: This service is deprecated and will be removed at some point. If you want to edit multiple transactions, please instead use the service 'Edit multiple transactions', where you can pass a comma-separated list of identifiers .

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | Comma-separated list of identifiers of updated transactions
body = swagger_client.UpdateTransactionsParams() # UpdateTransactionsParams | Update transactions parameters

try:
    # Edit multiple transactions (DEPRECATED)
    api_response = api_instance.edit_multiple_transactions_deprecated(ids, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->edit_multiple_transactions_deprecated: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| Comma-separated list of identifiers of updated transactions | 
 **body** | [**UpdateTransactionsParams**](UpdateTransactionsParams.md)| Update transactions parameters | 

### Return type

[**IdentifierList**](IdentifierList.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_transaction**
> Transaction edit_transaction(id, body)

Edit a transaction

Change a transaction's fields. You can change the following fields: 'isNew=true|false' and/or 'isPotentialDuplicate=false' and/or 'categoryId=<id>' and/or 'labelIds=[<ids>]'. To clear a transaction's category (so that it is no longer categorized), pass the value '0' as the categoryId. To clear the labels of the given transaction, pass an empty array of label identifiers: '[]'.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Identifier of transaction
body = swagger_client.UpdateTransactionsParams() # UpdateTransactionsParams | Update transactions parameters

try:
    # Edit a transaction
    api_response = api_instance.edit_transaction(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->edit_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identifier of transaction | 
 **body** | [**UpdateTransactionsParams**](UpdateTransactionsParams.md)| Update transactions parameters | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_and_search_all_transactions**
> PageableTransactionList get_and_search_all_transactions(view, ids=ids, search=search, counterpart=counterpart, account_ids=account_ids, min_bank_booking_date=min_bank_booking_date, max_bank_booking_date=max_bank_booking_date, min_finapi_booking_date=min_finapi_booking_date, max_finapi_booking_date=max_finapi_booking_date, min_amount=min_amount, max_amount=max_amount, direction=direction, label_ids=label_ids, category_ids=category_ids, include_child_categories=include_child_categories, is_new=is_new, is_potential_duplicate=is_potential_duplicate, is_adjusting_entry=is_adjusting_entry, min_import_date=min_import_date, max_import_date=max_import_date, page=page, per_page=per_page, order=order)

Get and search all transactions

Get transactions of the user that is authorized by the access_token. Must pass the user's access_token. You can set optional search criteria to get only those transactions that you are interested in. If you do not specify any search criteria, then this service functions as a 'get all' service.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
view = 'view_example' # str | This parameter defines finAPI's logical view on the transactions when querying them: 'bankView' regards only the original transactions as they were received from the bank, without considering how the transactions might have gotten split by the user (see POST /transactions/<id>/split). This means that if a transaction is split into logical sub-transactions, then the service will still regard only the original transaction, and NOT the logical sub-transactions in its processing (though for convenience, the transactions will have the data of their sub-transactions included in the response). 'userView' by contrast regards the transactions as they exist for the user. For transactions that have not been split into logical sub-transactions, there is no difference to the \"bankView\". But for transaction that have been split into logical sub-transactions, the service will ONLY regard these sub-transactions, and not the originally received transaction (though for convenience, the sub-transactions will have the identifier of their original transaction included in the response).
ids = [56] # list[int] | A comma-separated list of transaction identifiers. If specified, then only transactions whose identifier match any of the given identifiers will be regarded. The maximum number of identifiers is 1000. (optional)
search = 'search_example' # str | If specified, then only those transactions will be contained in the result whose 'purpose' or counterpart fields contain the given search string (the matching works case-insensitive). If no transactions contain the search string in any of these fields, then the result will be an empty list. NOTE: If the given search string consists of several terms (separated by whitespace), then ALL of these terms must be contained in the searched fields in order for a transaction to get included into the result. (optional)
counterpart = 'counterpart_example' # str | If specified, then only those transactions will be contained in the result whose counterpart fields contain the given search string (the matching works case-insensitive). If no transactions contain the search string in any of the counterpart fields, then the result will be an empty list. NOTE: If the given search string consists of several terms (separated by whitespace), then ALL of these terms must be contained in the searched fields in order for a transaction to get included into the result. (optional)
account_ids = [56] # list[int] | A comma-separated list of account identifiers. If specified, then only transactions that relate to the given accounts will be regarded. If not specified, then all accounts will be regarded. (optional)
min_bank_booking_date = 'min_bank_booking_date_example' # str | Lower bound for a transaction's booking date as returned by the bank (= original booking date), in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). If specified, then only transactions whose 'bankBookingDate' is equal to or later than the given date will be regarded. (optional)
max_bank_booking_date = 'max_bank_booking_date_example' # str | Upper bound for a transaction's booking date as returned by the bank (= original booking date), in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). If specified, then only transactions whose 'bankBookingDate' is equal to or earlier than the given date will be regarded. (optional)
min_finapi_booking_date = 'min_finapi_booking_date_example' # str | Lower bound for a transaction's booking date as set by finAPI, in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). For details about the meaning of the finAPI booking date, please see the field's documentation in the service's response. (optional)
max_finapi_booking_date = 'max_finapi_booking_date_example' # str | Upper bound for a transaction's booking date as set by finAPI, in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). For details about the meaning of the finAPI booking date, please see the field's documentation in the service's response. (optional)
min_amount = 8.14 # float | If specified, then only transactions whose amount is equal to or greater than the given amount will be regarded. Can contain a positive or negative number with at most two decimal places. Examples: -300.12, or 90.95 (optional)
max_amount = 8.14 # float | If specified, then only transactions whose amount is equal to or less than the given amount will be regarded. Can contain a positive or negative number with at most two decimal places. Examples: -300.12, or 90.95 (optional)
direction = 'all' # str | If specified, then only transactions with the given direction(s) will be regarded. Use 'income' for regarding only received payments (amount >= 0), 'spending' for regarding only outgoing payments (amount < 0), or 'all' to regard both directions. If not specified, the direction defaults to 'all'. (optional) (default to all)
label_ids = [56] # list[int] | A comma-separated list of label identifiers. If specified, then only transactions that have been marked with at least one of the given labels will be contained in the result. (optional)
category_ids = [56] # list[int] | A comma-separated list of category identifiers. If specified, then the result will contain only transactions whose category is either one of the given categories, or - but only if the 'includeChildCategories' flag is set to 'true' - whose category is a sub-category of one of the given categories. To include transactions without any category, pass the value '0' as the categoryId. (optional)
include_child_categories = true # bool | This flag controls how the given 'categoryIds' are handled. If set to 'true', then all transactions of a given categoryId, as well as all transactions of any of its sub-categories will be regarded. If set to 'false', then sub-categories of a given categoryId will not be regarded and only those transactions are regarded whose category matches one of the explicitly given categoryIds. The default value for this flag is 'true'. (optional) (default to true)
is_new = true # bool | If specified, then only transactions that have their 'isNew' flag set to true/false will be regarded. (optional)
is_potential_duplicate = true # bool | If specified, then only transactions that have their 'isPotentialDuplicate' flag set to true/false will be regarded. (optional)
is_adjusting_entry = true # bool | If specified, then only transactions that have their 'isAdjustingEntry' flag set to true/false will be regarded. (optional)
min_import_date = 'min_import_date_example' # str | Lower bound for a transaction's import date, in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). If specified, then only transactions whose 'importDate' is equal to or later than the given date will be regarded. (optional)
max_import_date = 'max_import_date_example' # str | Upper bound for a transaction's import date, in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). If specified, then only transactions whose 'importDate' is equal to or earlier than the given date will be regarded. (optional)
page = 1 # int | Result page that you want to retrieve. (optional) (default to 1)
per_page = 20 # int | Maximum number of records per page. Can be at most 500. NOTE: Due to its validation and visualization, the swagger frontend might show very low performance, or even crashes, when a service responds with a lot of data. It is recommended to use a HTTP client like Postman or DHC instead of our swagger frontend for service calls with large page sizes. (optional) (default to 20)
order = ['order_example'] # list[str] | Determines the order of the results. You can use the following fields for ordering the response: 'id', 'parentId', 'accountId', 'valueDate', 'bankBookingDate', 'finapiBookingDate', 'amount', 'purpose', 'counterpartName', 'counterpartAccountNumber', 'counterpartIban', 'counterpartBlz', 'counterpartBic', 'type', 'primanota', 'category.id', 'category.name', 'isPotentialDuplicate', 'isNew' and 'importDate'. The default order for all services is 'id,asc'. You can also order by multiple properties. In that case the order of the parameters passed is important. Example: '/transactions?order=finapiBookingDate,desc&order=counterpartName' will return the latest transactions first. If there are more transactions on the same day, then these transactions are ordered by the counterpart name (ascending). The general format is: 'property[,asc|desc]', with 'asc' being the default value. Please note that ordering by multiple fields is not supported in our swagger frontend, but you can test this feature with any HTTP tool of your choice (e.g. postman or DHC).  (optional)

try:
    # Get and search all transactions
    api_response = api_instance.get_and_search_all_transactions(view, ids=ids, search=search, counterpart=counterpart, account_ids=account_ids, min_bank_booking_date=min_bank_booking_date, max_bank_booking_date=max_bank_booking_date, min_finapi_booking_date=min_finapi_booking_date, max_finapi_booking_date=max_finapi_booking_date, min_amount=min_amount, max_amount=max_amount, direction=direction, label_ids=label_ids, category_ids=category_ids, include_child_categories=include_child_categories, is_new=is_new, is_potential_duplicate=is_potential_duplicate, is_adjusting_entry=is_adjusting_entry, min_import_date=min_import_date, max_import_date=max_import_date, page=page, per_page=per_page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_and_search_all_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view** | **str**| This parameter defines finAPI&#39;s logical view on the transactions when querying them: &#39;bankView&#39; regards only the original transactions as they were received from the bank, without considering how the transactions might have gotten split by the user (see POST /transactions/&lt;id&gt;/split). This means that if a transaction is split into logical sub-transactions, then the service will still regard only the original transaction, and NOT the logical sub-transactions in its processing (though for convenience, the transactions will have the data of their sub-transactions included in the response). &#39;userView&#39; by contrast regards the transactions as they exist for the user. For transactions that have not been split into logical sub-transactions, there is no difference to the \&quot;bankView\&quot;. But for transaction that have been split into logical sub-transactions, the service will ONLY regard these sub-transactions, and not the originally received transaction (though for convenience, the sub-transactions will have the identifier of their original transaction included in the response). | 
 **ids** | [**list[int]**](int.md)| A comma-separated list of transaction identifiers. If specified, then only transactions whose identifier match any of the given identifiers will be regarded. The maximum number of identifiers is 1000. | [optional] 
 **search** | **str**| If specified, then only those transactions will be contained in the result whose &#39;purpose&#39; or counterpart fields contain the given search string (the matching works case-insensitive). If no transactions contain the search string in any of these fields, then the result will be an empty list. NOTE: If the given search string consists of several terms (separated by whitespace), then ALL of these terms must be contained in the searched fields in order for a transaction to get included into the result. | [optional] 
 **counterpart** | **str**| If specified, then only those transactions will be contained in the result whose counterpart fields contain the given search string (the matching works case-insensitive). If no transactions contain the search string in any of the counterpart fields, then the result will be an empty list. NOTE: If the given search string consists of several terms (separated by whitespace), then ALL of these terms must be contained in the searched fields in order for a transaction to get included into the result. | [optional] 
 **account_ids** | [**list[int]**](int.md)| A comma-separated list of account identifiers. If specified, then only transactions that relate to the given accounts will be regarded. If not specified, then all accounts will be regarded. | [optional] 
 **min_bank_booking_date** | **str**| Lower bound for a transaction&#39;s booking date as returned by the bank (&#x3D; original booking date), in the format &#39;YYYY-MM-DD&#39; (e.g. &#39;2016-01-01&#39;). If specified, then only transactions whose &#39;bankBookingDate&#39; is equal to or later than the given date will be regarded. | [optional] 
 **max_bank_booking_date** | **str**| Upper bound for a transaction&#39;s booking date as returned by the bank (&#x3D; original booking date), in the format &#39;YYYY-MM-DD&#39; (e.g. &#39;2016-01-01&#39;). If specified, then only transactions whose &#39;bankBookingDate&#39; is equal to or earlier than the given date will be regarded. | [optional] 
 **min_finapi_booking_date** | **str**| Lower bound for a transaction&#39;s booking date as set by finAPI, in the format &#39;YYYY-MM-DD&#39; (e.g. &#39;2016-01-01&#39;). For details about the meaning of the finAPI booking date, please see the field&#39;s documentation in the service&#39;s response. | [optional] 
 **max_finapi_booking_date** | **str**| Upper bound for a transaction&#39;s booking date as set by finAPI, in the format &#39;YYYY-MM-DD&#39; (e.g. &#39;2016-01-01&#39;). For details about the meaning of the finAPI booking date, please see the field&#39;s documentation in the service&#39;s response. | [optional] 
 **min_amount** | **float**| If specified, then only transactions whose amount is equal to or greater than the given amount will be regarded. Can contain a positive or negative number with at most two decimal places. Examples: -300.12, or 90.95 | [optional] 
 **max_amount** | **float**| If specified, then only transactions whose amount is equal to or less than the given amount will be regarded. Can contain a positive or negative number with at most two decimal places. Examples: -300.12, or 90.95 | [optional] 
 **direction** | **str**| If specified, then only transactions with the given direction(s) will be regarded. Use &#39;income&#39; for regarding only received payments (amount &gt;&#x3D; 0), &#39;spending&#39; for regarding only outgoing payments (amount &lt; 0), or &#39;all&#39; to regard both directions. If not specified, the direction defaults to &#39;all&#39;. | [optional] [default to all]
 **label_ids** | [**list[int]**](int.md)| A comma-separated list of label identifiers. If specified, then only transactions that have been marked with at least one of the given labels will be contained in the result. | [optional] 
 **category_ids** | [**list[int]**](int.md)| A comma-separated list of category identifiers. If specified, then the result will contain only transactions whose category is either one of the given categories, or - but only if the &#39;includeChildCategories&#39; flag is set to &#39;true&#39; - whose category is a sub-category of one of the given categories. To include transactions without any category, pass the value &#39;0&#39; as the categoryId. | [optional] 
 **include_child_categories** | **bool**| This flag controls how the given &#39;categoryIds&#39; are handled. If set to &#39;true&#39;, then all transactions of a given categoryId, as well as all transactions of any of its sub-categories will be regarded. If set to &#39;false&#39;, then sub-categories of a given categoryId will not be regarded and only those transactions are regarded whose category matches one of the explicitly given categoryIds. The default value for this flag is &#39;true&#39;. | [optional] [default to true]
 **is_new** | **bool**| If specified, then only transactions that have their &#39;isNew&#39; flag set to true/false will be regarded. | [optional] 
 **is_potential_duplicate** | **bool**| If specified, then only transactions that have their &#39;isPotentialDuplicate&#39; flag set to true/false will be regarded. | [optional] 
 **is_adjusting_entry** | **bool**| If specified, then only transactions that have their &#39;isAdjustingEntry&#39; flag set to true/false will be regarded. | [optional] 
 **min_import_date** | **str**| Lower bound for a transaction&#39;s import date, in the format &#39;YYYY-MM-DD&#39; (e.g. &#39;2016-01-01&#39;). If specified, then only transactions whose &#39;importDate&#39; is equal to or later than the given date will be regarded. | [optional] 
 **max_import_date** | **str**| Upper bound for a transaction&#39;s import date, in the format &#39;YYYY-MM-DD&#39; (e.g. &#39;2016-01-01&#39;). If specified, then only transactions whose &#39;importDate&#39; is equal to or earlier than the given date will be regarded. | [optional] 
 **page** | **int**| Result page that you want to retrieve. | [optional] [default to 1]
 **per_page** | **int**| Maximum number of records per page. Can be at most 500. NOTE: Due to its validation and visualization, the swagger frontend might show very low performance, or even crashes, when a service responds with a lot of data. It is recommended to use a HTTP client like Postman or DHC instead of our swagger frontend for service calls with large page sizes. | [optional] [default to 20]
 **order** | [**list[str]**](str.md)| Determines the order of the results. You can use the following fields for ordering the response: &#39;id&#39;, &#39;parentId&#39;, &#39;accountId&#39;, &#39;valueDate&#39;, &#39;bankBookingDate&#39;, &#39;finapiBookingDate&#39;, &#39;amount&#39;, &#39;purpose&#39;, &#39;counterpartName&#39;, &#39;counterpartAccountNumber&#39;, &#39;counterpartIban&#39;, &#39;counterpartBlz&#39;, &#39;counterpartBic&#39;, &#39;type&#39;, &#39;primanota&#39;, &#39;category.id&#39;, &#39;category.name&#39;, &#39;isPotentialDuplicate&#39;, &#39;isNew&#39; and &#39;importDate&#39;. The default order for all services is &#39;id,asc&#39;. You can also order by multiple properties. In that case the order of the parameters passed is important. Example: &#39;/transactions?order&#x3D;finapiBookingDate,desc&amp;order&#x3D;counterpartName&#39; will return the latest transactions first. If there are more transactions on the same day, then these transactions are ordered by the counterpart name (ascending). The general format is: &#39;property[,asc|desc]&#39;, with &#39;asc&#39; being the default value. Please note that ordering by multiple fields is not supported in our swagger frontend, but you can test this feature with any HTTP tool of your choice (e.g. postman or DHC).  | [optional] 

### Return type

[**PageableTransactionList**](PageableTransactionList.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multiple_transactions**
> TransactionList get_multiple_transactions(ids)

Get multiple transactions

Get a list of multiple transactions of the user that is authorized by the access_token. Must pass the transactions' identifiers and the user's access_token. Transactions whose identifiers do not exist or do not relate to the authorized user will not be contained in the result (If this applies to all of the given identifiers, then the result will be an empty list). WARNING: This service is deprecated and will be removed at some point. If you want to get multiple transactions, please instead use the service 'Get and search all transactions', where you can pass a comma-separated list of identifiers .

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | Comma-separated list of identifiers of requested transactions

try:
    # Get multiple transactions
    api_response = api_instance.get_multiple_transactions(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_multiple_transactions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| Comma-separated list of identifiers of requested transactions | 

### Return type

[**TransactionList**](TransactionList.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transaction**
> Transaction get_transaction(id)

Get a transaction

Get a single transaction of the user that is authorized by the access_token. Must pass the transaction's identifier and the user's access_token.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Identifier of transaction

try:
    # Get a transaction
    api_response = api_instance.get_transaction(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->get_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Identifier of transaction | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_transaction**
> Transaction restore_transaction(id)

Restore a transaction

Restore a previously split transaction. Removes all of its sub-transactions.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Transaction identifier

try:
    # Restore a transaction
    api_response = api_instance.restore_transaction(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->restore_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Transaction identifier | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **split_transaction**
> Transaction split_transaction(id, body)

Split a transaction

Split a transaction into several logical sub-transactions. If the given transaction is split already, all its current sub-transactions will get deleted before the new sub-transactions will get created.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
id = 789 # int | Transaction identifier
body = swagger_client.SplitTransactionsParams() # SplitTransactionsParams | Split transactions parameters

try:
    # Split a transaction
    api_response = api_instance.split_transaction(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TransactionsApi->split_transaction: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Transaction identifier | 
 **body** | [**SplitTransactionsParams**](SplitTransactionsParams.md)| Split transactions parameters | 

### Return type

[**Transaction**](Transaction.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_categorization**
> trigger_categorization(body)

Trigger categorization

Triggers finAPI's background categorization process for all uncategorized transactions of the given bank connection(s) (or of all of the user's bank connections, if no bank connection identifiers are passed). The service returns as soon as the categorizations are scheduled. At this point, the bank connections will have their 'categorizationStatus' set to 'PENDING'. Use the service \"Get a bank connection\" or \"Get all bank connections\" to check when the categorization has finished (this is the case when the categorizationStatus has switched to 'READY').<br/><br/>Note that if at least one of the target bank connections is currently locked at the time when you call this service (i.e. the bank connection is currently being updated, or another categorization is already scheduled for it), then no categorization will be triggered at all and the service will respond with HTTP code 422.<br/><br/>Please also note:<br/>&bull; finAPI's background categorization process is executed automatically whenever you import or update a bank connection (though in case of update, it will categorize only the new transactions, and not re-run categorization for previously imported transactions). This means that in general you do not have to call this service after an import or update. Use this service only when you wish to re-run the categorization of all existing uncategorized transactions.<br/>&bull; if you wish to just manually assign categories to transactions, please use the service \"Edit a transaction\" or \"Edit multiple transactions\" instead.

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
api_instance = swagger_client.TransactionsApi(swagger_client.ApiClient(configuration))
body = swagger_client.TriggerCategorizationParams() # TriggerCategorizationParams | Trigger categorization parameters

try:
    # Trigger categorization
    api_instance.trigger_categorization(body)
except ApiException as e:
    print("Exception when calling TransactionsApi->trigger_categorization: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TriggerCategorizationParams**](TriggerCategorizationParams.md)| Trigger categorization parameters | 

### Return type

void (empty response body)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

