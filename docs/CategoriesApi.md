# swagger_client.CategoriesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_category**](CategoriesApi.md#create_category) | **POST** /api/v1/categories | Create a new category
[**delete_all_categories**](CategoriesApi.md#delete_all_categories) | **DELETE** /api/v1/categories | Delete all categories
[**delete_category**](CategoriesApi.md#delete_category) | **DELETE** /api/v1/categories/{id} | Delete a category
[**get_and_search_all_categories**](CategoriesApi.md#get_and_search_all_categories) | **GET** /api/v1/categories | Get and search all categories
[**get_cash_flows**](CategoriesApi.md#get_cash_flows) | **GET** /api/v1/categories/cashFlows | Get cash flows
[**get_category**](CategoriesApi.md#get_category) | **GET** /api/v1/categories/{id} | Get a category
[**get_multiple_categories**](CategoriesApi.md#get_multiple_categories) | **GET** /api/v1/categories/{ids} | Get multiple categories


# **create_category**
> Category create_category(body=body)

Create a new category

Create a new custom category for the authorized user. Must pass the user's access_token.

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
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))
body = swagger_client.CategoryParams() # CategoryParams | Parameters of the new category (optional)

try:
    # Create a new category
    api_response = api_instance.create_category(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->create_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CategoryParams**](CategoryParams.md)| Parameters of the new category | [optional] 

### Return type

[**Category**](Category.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_all_categories**
> IdentifierList delete_all_categories()

Delete all categories

Delete all custom categories of the user that is authorized by the access_token. Must pass the user's access_token. Note that this deletes both parent categories as well as any related sub-categories.

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
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))

try:
    # Delete all categories
    api_response = api_instance.delete_all_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->delete_all_categories: %s\n" % e)
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

# **delete_category**
> delete_category(id)

Delete a category

Delete a single category of the user that is authorized by the access_token. Must pass the user's access_token. Note that you can only delete user-custom categories (category's where the 'isCustom' flag is true). Also note that when deleting a parent category, all its sub-categories will be deleted as well.

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
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Category identifier

try:
    # Delete a category
    api_instance.delete_category(id)
except ApiException as e:
    print("Exception when calling CategoriesApi->delete_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Category identifier | 

### Return type

void (empty response body)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_and_search_all_categories**
> PageableCategoryList get_and_search_all_categories(ids=ids, search=search, is_custom=is_custom, page=page, per_page=per_page, order=order)

Get and search all categories

Get a list of all global finAPI categories as well as all custom categories of the authorized user. Must pass the user's access_token. You can set optional search criteria to get only those categories that you are interested in. If you do not specify any search criteria, then this service functions as a 'get all' service.

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
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | A comma-separated list of category identifiers. If specified, then only categories whose identifier match any of the given identifiers will be regarded. The maximum number of identifiers is 1000. (optional)
search = 'search_example' # str | If specified, then only those categories will be contained in the result whose 'name' contains the given search string (the matching works case-insensitive). If no categories contain the search string in their name, then the result will be an empty list. NOTE: If the given search string consists of several terms (separated by whitespace), then ALL of these terms must be contained in the name in order for a category to get included into the result. (optional)
is_custom = true # bool | If specified, then the result will contain only categories that are either finAPI global (in case of value 'false'), or only categories that have been created by the authorized user (in case of value 'true'). (optional)
page = 1 # int | Result page that you want to retrieve. (optional) (default to 1)
per_page = 20 # int | Maximum number of records per page. Can be at most 500. NOTE: Due to its validation and visualization, the swagger frontend might show very low performance, or even crashes, when a service responds with a lot of data. It is recommended to use a HTTP client like Postman or DHC instead of our swagger frontend for service calls with large page sizes. (optional) (default to 20)
order = ['order_example'] # list[str] | Determines the order of the results. You can order the results by 'id', 'name' and 'isCustom'. The default order is 'id,asc'. You can also order by multiple properties. In that case the order of the parameters passed is important. Example: '/categories?order=isCustom,desc&order=name' will return all custom categories followed by all default categories. Both groups are ordered ascending by name. The general format is: 'property[,asc|desc]', with 'asc' being the default value. Please note that ordering by multiple fields is not supported in our swagger frontend, but you can test this feature with any HTTP tool of your choice (e.g. postman or DHC).  (optional)

try:
    # Get and search all categories
    api_response = api_instance.get_and_search_all_categories(ids=ids, search=search, is_custom=is_custom, page=page, per_page=per_page, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_and_search_all_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| A comma-separated list of category identifiers. If specified, then only categories whose identifier match any of the given identifiers will be regarded. The maximum number of identifiers is 1000. | [optional] 
 **search** | **str**| If specified, then only those categories will be contained in the result whose &#39;name&#39; contains the given search string (the matching works case-insensitive). If no categories contain the search string in their name, then the result will be an empty list. NOTE: If the given search string consists of several terms (separated by whitespace), then ALL of these terms must be contained in the name in order for a category to get included into the result. | [optional] 
 **is_custom** | **bool**| If specified, then the result will contain only categories that are either finAPI global (in case of value &#39;false&#39;), or only categories that have been created by the authorized user (in case of value &#39;true&#39;). | [optional] 
 **page** | **int**| Result page that you want to retrieve. | [optional] [default to 1]
 **per_page** | **int**| Maximum number of records per page. Can be at most 500. NOTE: Due to its validation and visualization, the swagger frontend might show very low performance, or even crashes, when a service responds with a lot of data. It is recommended to use a HTTP client like Postman or DHC instead of our swagger frontend for service calls with large page sizes. | [optional] [default to 20]
 **order** | [**list[str]**](str.md)| Determines the order of the results. You can order the results by &#39;id&#39;, &#39;name&#39; and &#39;isCustom&#39;. The default order is &#39;id,asc&#39;. You can also order by multiple properties. In that case the order of the parameters passed is important. Example: &#39;/categories?order&#x3D;isCustom,desc&amp;order&#x3D;name&#39; will return all custom categories followed by all default categories. Both groups are ordered ascending by name. The general format is: &#39;property[,asc|desc]&#39;, with &#39;asc&#39; being the default value. Please note that ordering by multiple fields is not supported in our swagger frontend, but you can test this feature with any HTTP tool of your choice (e.g. postman or DHC).  | [optional] 

### Return type

[**PageableCategoryList**](PageableCategoryList.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cash_flows**
> CashFlowList get_cash_flows(search=search, counterpart=counterpart, account_ids=account_ids, min_bank_booking_date=min_bank_booking_date, max_bank_booking_date=max_bank_booking_date, min_finapi_booking_date=min_finapi_booking_date, max_finapi_booking_date=max_finapi_booking_date, min_amount=min_amount, max_amount=max_amount, direction=direction, label_ids=label_ids, category_ids=category_ids, is_new=is_new, min_import_date=min_import_date, max_import_date=max_import_date, include_sub_cash_flows=include_sub_cash_flows, order=order)

Get cash flows

Get the cash flow(s) (= total income, spending, and balance) for one or several categories. You can specify various criteria such as the time period to calculate the cash flows for, or what categories to do the calculations for. Note that the cash flow for a category may include the cash flows for all of its sub-categories, or not include it, depending on the 'includeSubCashFlows' setting. Must pass the user's access_token.

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
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))
search = 'search_example' # str | If specified, then only transactions that contain the search term in their purpose or counterpart fields will be contained in the result. Note that the search is case insensitive. (optional)
counterpart = 'counterpart_example' # str | The counterpart is the person or institution that received your payment, or that you made the payment to. If this parameter is specified, then only transactions that contain the given term in one (or more) of their counterpart fields ('counterpartName', 'counterpartAccountNumber', 'counterpartIban', 'counterpartBic' or 'counterpartBlz') will be contained in the result. Note that the search is case insensitive. (optional)
account_ids = [56] # list[int] | A comma-separated list of account identifiers. If specified, then only transactions that relate to the given accounts will be regarded. If not specified, then all accounts will be regarded. (optional)
min_bank_booking_date = 'min_bank_booking_date_example' # str | Lower bound for a transaction's booking date as returned by the bank (= original booking date), in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). If specified, then only transactions whose 'bankBookingDate' is equal to or later than the given date will be regarded. (optional)
max_bank_booking_date = 'max_bank_booking_date_example' # str | Upper bound for a transaction's booking date as returned by the bank (= original booking date), in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). If specified, then only transactions whose 'bankBookingDate' is equal to or earlier than the given date will be regarded. (optional)
min_finapi_booking_date = 'min_finapi_booking_date_example' # str | Lower bound for a transaction's booking date as set by finAPI, in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). For details about the meaning of the finAPI booking date, please see the field's documentation in the service's response. (optional)
max_finapi_booking_date = 'max_finapi_booking_date_example' # str | Upper bound for a transaction's booking date as set by finAPI, in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). For details about the meaning of the finAPI booking date, please see the field's documentation in the service's response. (optional)
min_amount = 8.14 # float | If specified, then only transactions whose amount is equal to or greater than the given amount will be regarded. Can contain a positive or negative number with at most two decimal places. Examples: -300.12, or 90.95 (optional)
max_amount = 8.14 # float | If specified, then only transactions whose amount is equal to or less than the given amount will be regarded. Can contain a positive or negative number with at most two decimal places. Examples: -300.12, or 90.95 (optional)
direction = 'all' # str | If specified, then only transactions with the given direction(s) will be regarded. Use 'income' for regarding only received payments (amount >= 0), 'spending' for regarding only outgoing payments (amount < 0), or 'all' to regard both directions. If not specified, the direction defaults to 'all'. (optional) (default to all)
label_ids = [56] # list[int] | A comma-separated list of label identifiers. If specified, then only transactions that have been marked with at least one of the given labels will be contained in the result. (optional)
category_ids = [56] # list[int] | If specified, then the result will contain only those cash flows that relate to the given categories. Note that the cash flow for a category may include/exclude the cash flows of its sub-categories, depending on the 'includeSubCashFlows' setting. To include the cash flow of not categorized transactions, pass the value '0' as categoryId. Note: When this parameter is NOT set, then the result will contain a cash flow for all categories that have transactions associated to them (this includes the 'null'-category for the cash flow of not categorized transactions), more precisely: transactions that fulfill the filter criteria. Categories that have no associated transactions according to the filter criteria will not appear in the result. However, when you specify this parameter, then all specified categories will have a cash flow entry in the result, even if there are no associated transactions for the category (the cash flow will have income, spending and balance all set to zero). (optional)
is_new = true # bool | If specified, then only transactions that have their 'isNew' flag set to true/false will be regarded for the cash flow calculations. (optional)
min_import_date = 'min_import_date_example' # str | Lower bound for a transaction's import date, in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). If specified, then only transactions whose 'importDate' is equal to or later than the given date will be regarded. (optional)
max_import_date = 'max_import_date_example' # str | Upper bound for a transaction's import date, in the format 'YYYY-MM-DD' (e.g. '2016-01-01'). If specified, then only transactions whose 'importDate' is equal to or earlier than the given date will be regarded. (optional)
include_sub_cash_flows = true # bool | If it is true, then the income, spending and balance of a main category results from all transactions that have either this (main) category or any of its subcategories assigned (of course all transactions depends from the other filtering settings); If it is false, then the income, spending and balance of a main category only results from the transactions that have exactly this (main) category assigned. Default value for this parameter is 'true'. (optional) (default to true)
order = ['order_example'] # list[str] | Determines the order of the results. You can order the results by 'income', 'spending', 'balance', 'category.id' or 'category.name'. The default order for this service is 'category.id,asc'. You can also order by multiple properties. In that case the order of the parameters passed is important. Example: '/cashFlows?order=income,desc&order=spending,asc&balance,desc' will return as first result the category with the highest income. If two categories have the same income, it returns the category with the highest spending first (because spending is a negative value) and so on. The general format is: 'property[,asc|desc]', with 'asc' being the default value. Please note that ordering by multiple fields is not supported in our swagger frontend, but you can test this feature with any HTTP tool of your choice (e.g. postman or DHC).  (optional)

try:
    # Get cash flows
    api_response = api_instance.get_cash_flows(search=search, counterpart=counterpart, account_ids=account_ids, min_bank_booking_date=min_bank_booking_date, max_bank_booking_date=max_bank_booking_date, min_finapi_booking_date=min_finapi_booking_date, max_finapi_booking_date=max_finapi_booking_date, min_amount=min_amount, max_amount=max_amount, direction=direction, label_ids=label_ids, category_ids=category_ids, is_new=is_new, min_import_date=min_import_date, max_import_date=max_import_date, include_sub_cash_flows=include_sub_cash_flows, order=order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_cash_flows: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search** | **str**| If specified, then only transactions that contain the search term in their purpose or counterpart fields will be contained in the result. Note that the search is case insensitive. | [optional] 
 **counterpart** | **str**| The counterpart is the person or institution that received your payment, or that you made the payment to. If this parameter is specified, then only transactions that contain the given term in one (or more) of their counterpart fields (&#39;counterpartName&#39;, &#39;counterpartAccountNumber&#39;, &#39;counterpartIban&#39;, &#39;counterpartBic&#39; or &#39;counterpartBlz&#39;) will be contained in the result. Note that the search is case insensitive. | [optional] 
 **account_ids** | [**list[int]**](int.md)| A comma-separated list of account identifiers. If specified, then only transactions that relate to the given accounts will be regarded. If not specified, then all accounts will be regarded. | [optional] 
 **min_bank_booking_date** | **str**| Lower bound for a transaction&#39;s booking date as returned by the bank (&#x3D; original booking date), in the format &#39;YYYY-MM-DD&#39; (e.g. &#39;2016-01-01&#39;). If specified, then only transactions whose &#39;bankBookingDate&#39; is equal to or later than the given date will be regarded. | [optional] 
 **max_bank_booking_date** | **str**| Upper bound for a transaction&#39;s booking date as returned by the bank (&#x3D; original booking date), in the format &#39;YYYY-MM-DD&#39; (e.g. &#39;2016-01-01&#39;). If specified, then only transactions whose &#39;bankBookingDate&#39; is equal to or earlier than the given date will be regarded. | [optional] 
 **min_finapi_booking_date** | **str**| Lower bound for a transaction&#39;s booking date as set by finAPI, in the format &#39;YYYY-MM-DD&#39; (e.g. &#39;2016-01-01&#39;). For details about the meaning of the finAPI booking date, please see the field&#39;s documentation in the service&#39;s response. | [optional] 
 **max_finapi_booking_date** | **str**| Upper bound for a transaction&#39;s booking date as set by finAPI, in the format &#39;YYYY-MM-DD&#39; (e.g. &#39;2016-01-01&#39;). For details about the meaning of the finAPI booking date, please see the field&#39;s documentation in the service&#39;s response. | [optional] 
 **min_amount** | **float**| If specified, then only transactions whose amount is equal to or greater than the given amount will be regarded. Can contain a positive or negative number with at most two decimal places. Examples: -300.12, or 90.95 | [optional] 
 **max_amount** | **float**| If specified, then only transactions whose amount is equal to or less than the given amount will be regarded. Can contain a positive or negative number with at most two decimal places. Examples: -300.12, or 90.95 | [optional] 
 **direction** | **str**| If specified, then only transactions with the given direction(s) will be regarded. Use &#39;income&#39; for regarding only received payments (amount &gt;&#x3D; 0), &#39;spending&#39; for regarding only outgoing payments (amount &lt; 0), or &#39;all&#39; to regard both directions. If not specified, the direction defaults to &#39;all&#39;. | [optional] [default to all]
 **label_ids** | [**list[int]**](int.md)| A comma-separated list of label identifiers. If specified, then only transactions that have been marked with at least one of the given labels will be contained in the result. | [optional] 
 **category_ids** | [**list[int]**](int.md)| If specified, then the result will contain only those cash flows that relate to the given categories. Note that the cash flow for a category may include/exclude the cash flows of its sub-categories, depending on the &#39;includeSubCashFlows&#39; setting. To include the cash flow of not categorized transactions, pass the value &#39;0&#39; as categoryId. Note: When this parameter is NOT set, then the result will contain a cash flow for all categories that have transactions associated to them (this includes the &#39;null&#39;-category for the cash flow of not categorized transactions), more precisely: transactions that fulfill the filter criteria. Categories that have no associated transactions according to the filter criteria will not appear in the result. However, when you specify this parameter, then all specified categories will have a cash flow entry in the result, even if there are no associated transactions for the category (the cash flow will have income, spending and balance all set to zero). | [optional] 
 **is_new** | **bool**| If specified, then only transactions that have their &#39;isNew&#39; flag set to true/false will be regarded for the cash flow calculations. | [optional] 
 **min_import_date** | **str**| Lower bound for a transaction&#39;s import date, in the format &#39;YYYY-MM-DD&#39; (e.g. &#39;2016-01-01&#39;). If specified, then only transactions whose &#39;importDate&#39; is equal to or later than the given date will be regarded. | [optional] 
 **max_import_date** | **str**| Upper bound for a transaction&#39;s import date, in the format &#39;YYYY-MM-DD&#39; (e.g. &#39;2016-01-01&#39;). If specified, then only transactions whose &#39;importDate&#39; is equal to or earlier than the given date will be regarded. | [optional] 
 **include_sub_cash_flows** | **bool**| If it is true, then the income, spending and balance of a main category results from all transactions that have either this (main) category or any of its subcategories assigned (of course all transactions depends from the other filtering settings); If it is false, then the income, spending and balance of a main category only results from the transactions that have exactly this (main) category assigned. Default value for this parameter is &#39;true&#39;. | [optional] [default to true]
 **order** | [**list[str]**](str.md)| Determines the order of the results. You can order the results by &#39;income&#39;, &#39;spending&#39;, &#39;balance&#39;, &#39;category.id&#39; or &#39;category.name&#39;. The default order for this service is &#39;category.id,asc&#39;. You can also order by multiple properties. In that case the order of the parameters passed is important. Example: &#39;/cashFlows?order&#x3D;income,desc&amp;order&#x3D;spending,asc&amp;balance,desc&#39; will return as first result the category with the highest income. If two categories have the same income, it returns the category with the highest spending first (because spending is a negative value) and so on. The general format is: &#39;property[,asc|desc]&#39;, with &#39;asc&#39; being the default value. Please note that ordering by multiple fields is not supported in our swagger frontend, but you can test this feature with any HTTP tool of your choice (e.g. postman or DHC).  | [optional] 

### Return type

[**CashFlowList**](CashFlowList.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_category**
> Category get_category(id)

Get a category

Get a single category that is either a global finAPI category or a custom category of the authorized user. Must pass the category's identifier and the user's access_token.

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
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))
id = 789 # int | Category identifier

try:
    # Get a category
    api_response = api_instance.get_category(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_category: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Category identifier | 

### Return type

[**Category**](Category.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_multiple_categories**
> CategoryList get_multiple_categories(ids)

Get multiple categories

Get a list of multiple categories that are either a global finAPI category or a custom category of the authorized user. Must pass the categories' identifiers and the user's access_token. Categories whose identifiers do not exist or that relate to a different user not be contained in the result (If this applies to all of the given identifiers, then the result will be an empty list). WARNING: This service is deprecated and will be removed at some point. If you want to get multiple categories, please instead use the service 'Get and search all categories' and pass a comma-separated list of identifiers as a parameter 'ids'.

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
api_instance = swagger_client.CategoriesApi(swagger_client.ApiClient(configuration))
ids = [56] # list[int] | Comma-separated list of identifiers of requested categories

try:
    # Get multiple categories
    api_response = api_instance.get_multiple_categories(ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CategoriesApi->get_multiple_categories: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| Comma-separated list of identifiers of requested categories | 

### Return type

[**CategoryList**](CategoryList.md)

### Authorization

[finapi_auth](../README.md#finapi_auth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

