# swagger-client
finAPI RESTful Services

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1.41.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: finapi_auth
swagger_client.configuration.access_token = 'YOUR_ACCESS_TOKEN'
# create an instance of the API class
api_instance = swagger_client.AccountsApi()
id = 789 # int | Identifier of the account to delete

try:
    # Delete an account
    api_instance.delete_account(id)
except ApiException as e:
    print("Exception when calling AccountsApi->delete_account: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**delete_account**](docs/AccountsApi.md#delete_account) | **DELETE** /api/v1/accounts/{id} | Delete an account
*AccountsApi* | [**delete_all_accounts**](docs/AccountsApi.md#delete_all_accounts) | **DELETE** /api/v1/accounts | Delete all accounts
*AccountsApi* | [**edit_account**](docs/AccountsApi.md#edit_account) | **PATCH** /api/v1/accounts/{id} | Edit an account
*AccountsApi* | [**execute_sepa_direct_debit**](docs/AccountsApi.md#execute_sepa_direct_debit) | **POST** /api/v1/accounts/executeSepaDirectDebit | Execute SEPA Direct Debit
*AccountsApi* | [**execute_sepa_money_transfer**](docs/AccountsApi.md#execute_sepa_money_transfer) | **POST** /api/v1/accounts/executeSepaMoneyTransfer | Execute SEPA Money Transfer
*AccountsApi* | [**get_account**](docs/AccountsApi.md#get_account) | **GET** /api/v1/accounts/{id} | Get an account
*AccountsApi* | [**get_and_search_all_accounts**](docs/AccountsApi.md#get_and_search_all_accounts) | **GET** /api/v1/accounts | Get and search all accounts
*AccountsApi* | [**get_daily_balances**](docs/AccountsApi.md#get_daily_balances) | **GET** /api/v1/accounts/dailyBalances | Get daily balances
*AccountsApi* | [**get_multiple_accounts**](docs/AccountsApi.md#get_multiple_accounts) | **GET** /api/v1/accounts/{ids} | Get multiple accounts
*AccountsApi* | [**request_sepa_direct_debit**](docs/AccountsApi.md#request_sepa_direct_debit) | **POST** /api/v1/accounts/requestSepaDirectDebit | Request SEPA Direct Debit
*AccountsApi* | [**request_sepa_money_transfer**](docs/AccountsApi.md#request_sepa_money_transfer) | **POST** /api/v1/accounts/requestSepaMoneyTransfer | Request SEPA Money Transfer
*AuthorizationApi* | [**get_token**](docs/AuthorizationApi.md#get_token) | **POST** /oauth/token | Get tokens
*AuthorizationApi* | [**revoke_token**](docs/AuthorizationApi.md#revoke_token) | **POST** /oauth/revoke | Revoke a token
*BankConnectionsApi* | [**delete_all_bank_connections**](docs/BankConnectionsApi.md#delete_all_bank_connections) | **DELETE** /api/v1/bankConnections | Delete all bank connections
*BankConnectionsApi* | [**delete_bank_connection**](docs/BankConnectionsApi.md#delete_bank_connection) | **DELETE** /api/v1/bankConnections/{id} | Delete a bank connection
*BankConnectionsApi* | [**edit_bank_connection**](docs/BankConnectionsApi.md#edit_bank_connection) | **PATCH** /api/v1/bankConnections/{id} | Edit a bank connection
*BankConnectionsApi* | [**get_all_bank_connections**](docs/BankConnectionsApi.md#get_all_bank_connections) | **GET** /api/v1/bankConnections | Get all bank connections
*BankConnectionsApi* | [**get_bank_connection**](docs/BankConnectionsApi.md#get_bank_connection) | **GET** /api/v1/bankConnections/{id} | Get a bank connection
*BankConnectionsApi* | [**get_multiple_bank_connections**](docs/BankConnectionsApi.md#get_multiple_bank_connections) | **GET** /api/v1/bankConnections/{ids} | Get multiple bank connections
*BankConnectionsApi* | [**import_bank_connection**](docs/BankConnectionsApi.md#import_bank_connection) | **POST** /api/v1/bankConnections/import | Import a new bank connection
*BankConnectionsApi* | [**update_bank_connection**](docs/BankConnectionsApi.md#update_bank_connection) | **POST** /api/v1/bankConnections/update | Update a bank connection
*BanksApi* | [**get_and_search_all_banks**](docs/BanksApi.md#get_and_search_all_banks) | **GET** /api/v1/banks | Get and search all banks
*BanksApi* | [**get_bank**](docs/BanksApi.md#get_bank) | **GET** /api/v1/banks/{id} | Get a bank
*BanksApi* | [**get_multiple_banks**](docs/BanksApi.md#get_multiple_banks) | **GET** /api/v1/banks/{ids} | Get multiple banks
*CategoriesApi* | [**create_category**](docs/CategoriesApi.md#create_category) | **POST** /api/v1/categories | Create a new category
*CategoriesApi* | [**delete_all_categories**](docs/CategoriesApi.md#delete_all_categories) | **DELETE** /api/v1/categories | Delete all categories
*CategoriesApi* | [**delete_category**](docs/CategoriesApi.md#delete_category) | **DELETE** /api/v1/categories/{id} | Delete a category
*CategoriesApi* | [**get_and_search_all_categories**](docs/CategoriesApi.md#get_and_search_all_categories) | **GET** /api/v1/categories | Get and search all categories
*CategoriesApi* | [**get_cash_flows**](docs/CategoriesApi.md#get_cash_flows) | **GET** /api/v1/categories/cashFlows | Get cash flows
*CategoriesApi* | [**get_category**](docs/CategoriesApi.md#get_category) | **GET** /api/v1/categories/{id} | Get a category
*CategoriesApi* | [**get_multiple_categories**](docs/CategoriesApi.md#get_multiple_categories) | **GET** /api/v1/categories/{ids} | Get multiple categories
*ClientConfigurationApi* | [**edit_client_configuration**](docs/ClientConfigurationApi.md#edit_client_configuration) | **PATCH** /api/v1/clientConfiguration | Edit client configuration
*ClientConfigurationApi* | [**get_client_configuration**](docs/ClientConfigurationApi.md#get_client_configuration) | **GET** /api/v1/clientConfiguration | Get client configuration
*LabelsApi* | [**create_label**](docs/LabelsApi.md#create_label) | **POST** /api/v1/labels | Create a new label
*LabelsApi* | [**delete_all_labels**](docs/LabelsApi.md#delete_all_labels) | **DELETE** /api/v1/labels | Delete all labels
*LabelsApi* | [**delete_label**](docs/LabelsApi.md#delete_label) | **DELETE** /api/v1/labels/{id} | Delete a label
*LabelsApi* | [**edit_label**](docs/LabelsApi.md#edit_label) | **PATCH** /api/v1/labels/{id} | Edit a label
*LabelsApi* | [**get_and_search_all_labels**](docs/LabelsApi.md#get_and_search_all_labels) | **GET** /api/v1/labels | Get and search all labels
*LabelsApi* | [**get_label**](docs/LabelsApi.md#get_label) | **GET** /api/v1/labels/{id} | Get a label
*LabelsApi* | [**get_multiple_labels**](docs/LabelsApi.md#get_multiple_labels) | **GET** /api/v1/labels/{ids} | Get multiple labels
*MandatorAdministrationApi* | [**delete_users**](docs/MandatorAdministrationApi.md#delete_users) | **POST** /api/v1/mandatorAdmin/deleteUsers | Delete users
*MandatorAdministrationApi* | [**get_user_list**](docs/MandatorAdministrationApi.md#get_user_list) | **GET** /api/v1/mandatorAdmin/getUserList | Get user list
*MocksAndTestsApi* | [**mock_batch_update**](docs/MocksAndTestsApi.md#mock_batch_update) | **POST** /api/v1/tests/mockBatchUpdate | Mock batch update
*NotificationRulesApi* | [**create_notification_rule**](docs/NotificationRulesApi.md#create_notification_rule) | **POST** /api/v1/notificationRules | Create a new notification rule
*NotificationRulesApi* | [**delete_all_notification_rules**](docs/NotificationRulesApi.md#delete_all_notification_rules) | **DELETE** /api/v1/notificationRules | Delete all notification rules
*NotificationRulesApi* | [**delete_notification_rule**](docs/NotificationRulesApi.md#delete_notification_rule) | **DELETE** /api/v1/notificationRules/{id} | Delete a notification rule
*NotificationRulesApi* | [**get_and_search_all_notification_rules**](docs/NotificationRulesApi.md#get_and_search_all_notification_rules) | **GET** /api/v1/notificationRules | Get and search all notification rules
*NotificationRulesApi* | [**get_notification_rule**](docs/NotificationRulesApi.md#get_notification_rule) | **GET** /api/v1/notificationRules/{id} | Get a notification rule
*SecuritiesApi* | [**get_and_search_all_securities**](docs/SecuritiesApi.md#get_and_search_all_securities) | **GET** /api/v1/securities | Get and search all securities
*SecuritiesApi* | [**get_multiple_securities**](docs/SecuritiesApi.md#get_multiple_securities) | **GET** /api/v1/securities/{ids} | Get multiple securities
*SecuritiesApi* | [**get_security**](docs/SecuritiesApi.md#get_security) | **GET** /api/v1/securities/{id} | Get a security
*TransactionsApi* | [**delete_all_transactions**](docs/TransactionsApi.md#delete_all_transactions) | **DELETE** /api/v1/transactions | Delete all transactions
*TransactionsApi* | [**delete_transaction**](docs/TransactionsApi.md#delete_transaction) | **DELETE** /api/v1/transactions/{id} | Delete a transaction
*TransactionsApi* | [**edit_multiple_transactions**](docs/TransactionsApi.md#edit_multiple_transactions) | **PATCH** /api/v1/transactions | Edit multiple transactions
*TransactionsApi* | [**edit_multiple_transactions_deprecated**](docs/TransactionsApi.md#edit_multiple_transactions_deprecated) | **PATCH** /api/v1/transactions/{ids} | Edit multiple transactions (DEPRECATED)
*TransactionsApi* | [**edit_transaction**](docs/TransactionsApi.md#edit_transaction) | **PATCH** /api/v1/transactions/{id} | Edit a transaction
*TransactionsApi* | [**get_and_search_all_transactions**](docs/TransactionsApi.md#get_and_search_all_transactions) | **GET** /api/v1/transactions | Get and search all transactions
*TransactionsApi* | [**get_multiple_transactions**](docs/TransactionsApi.md#get_multiple_transactions) | **GET** /api/v1/transactions/{ids} | Get multiple transactions
*TransactionsApi* | [**get_transaction**](docs/TransactionsApi.md#get_transaction) | **GET** /api/v1/transactions/{id} | Get a transaction
*TransactionsApi* | [**restore_transaction**](docs/TransactionsApi.md#restore_transaction) | **POST** /api/v1/transactions/{id}/restore | Restore a transaction
*TransactionsApi* | [**split_transaction**](docs/TransactionsApi.md#split_transaction) | **POST** /api/v1/transactions/{id}/split | Split a transaction
*TransactionsApi* | [**trigger_categorization**](docs/TransactionsApi.md#trigger_categorization) | **POST** /api/v1/transactions/triggerCategorization | Trigger categorization
*UsersApi* | [**create_user**](docs/UsersApi.md#create_user) | **POST** /api/v1/users | Create a new user
*UsersApi* | [**delete_authorized_user**](docs/UsersApi.md#delete_authorized_user) | **DELETE** /api/v1/users | Delete the authorized user
*UsersApi* | [**delete_unverified_user**](docs/UsersApi.md#delete_unverified_user) | **DELETE** /api/v1/users/{userId} | Delete an unverified user
*UsersApi* | [**edit_authorized_user**](docs/UsersApi.md#edit_authorized_user) | **PATCH** /api/v1/users | Edit the authorized user
*UsersApi* | [**execute_password_change**](docs/UsersApi.md#execute_password_change) | **POST** /api/v1/users/executePasswordChange | Execute password change
*UsersApi* | [**get_authorized_user**](docs/UsersApi.md#get_authorized_user) | **GET** /api/v1/users | Get the authorized user
*UsersApi* | [**get_verification_status**](docs/UsersApi.md#get_verification_status) | **GET** /api/v1/users/verificationStatus | Get a user&#39;s verification status
*UsersApi* | [**request_password_change**](docs/UsersApi.md#request_password_change) | **POST** /api/v1/users/requestPasswordChange | Request password change
*UsersApi* | [**verify_user**](docs/UsersApi.md#verify_user) | **POST** /api/v1/users/verify/{userId} | Verify a user


## Documentation For Models

 - [AccessToken](docs/AccessToken.md)
 - [Account](docs/Account.md)
 - [AccountList](docs/AccountList.md)
 - [AccountParams](docs/AccountParams.md)
 - [BadCredentialsError](docs/BadCredentialsError.md)
 - [Bank](docs/Bank.md)
 - [BankConnection](docs/BankConnection.md)
 - [BankConnectionList](docs/BankConnectionList.md)
 - [BankList](docs/BankList.md)
 - [BankResponse](docs/BankResponse.md)
 - [CashFlow](docs/CashFlow.md)
 - [CashFlowList](docs/CashFlowList.md)
 - [Category](docs/Category.md)
 - [CategoryList](docs/CategoryList.md)
 - [CategoryParams](docs/CategoryParams.md)
 - [ClearingAccountData](docs/ClearingAccountData.md)
 - [ClientConfiguration](docs/ClientConfiguration.md)
 - [ClientConfigurationParams](docs/ClientConfigurationParams.md)
 - [DailyBalance](docs/DailyBalance.md)
 - [DailyBalanceList](docs/DailyBalanceList.md)
 - [DirectDebitOrderingResponse](docs/DirectDebitOrderingResponse.md)
 - [EditBankConnectionParams](docs/EditBankConnectionParams.md)
 - [ErrorDetails](docs/ErrorDetails.md)
 - [ErrorMessage](docs/ErrorMessage.md)
 - [ExecutePasswordChangeParams](docs/ExecutePasswordChangeParams.md)
 - [ExecuteSepaDirectDebitParams](docs/ExecuteSepaDirectDebitParams.md)
 - [ExecuteSepaMoneyTransferParams](docs/ExecuteSepaMoneyTransferParams.md)
 - [IdentifierList](docs/IdentifierList.md)
 - [ImportBankConnectionParams](docs/ImportBankConnectionParams.md)
 - [Label](docs/Label.md)
 - [LabelList](docs/LabelList.md)
 - [LabelParams](docs/LabelParams.md)
 - [MockAccountData](docs/MockAccountData.md)
 - [MockBankConnectionUpdate](docs/MockBankConnectionUpdate.md)
 - [MockBatchUpdateParams](docs/MockBatchUpdateParams.md)
 - [MoneyTransferOrderingResponse](docs/MoneyTransferOrderingResponse.md)
 - [MonthlyUserStats](docs/MonthlyUserStats.md)
 - [NewTransaction](docs/NewTransaction.md)
 - [NotificationRule](docs/NotificationRule.md)
 - [NotificationRuleList](docs/NotificationRuleList.md)
 - [NotificationRuleParams](docs/NotificationRuleParams.md)
 - [PageableBankList](docs/PageableBankList.md)
 - [PageableCategoryList](docs/PageableCategoryList.md)
 - [PageableLabelList](docs/PageableLabelList.md)
 - [PageableSecurityList](docs/PageableSecurityList.md)
 - [PageableTransactionList](docs/PageableTransactionList.md)
 - [PageableUserInfoList](docs/PageableUserInfoList.md)
 - [Paging](docs/Paging.md)
 - [PasswordChangingResource](docs/PasswordChangingResource.md)
 - [PaypalTransactionData](docs/PaypalTransactionData.md)
 - [RequestPasswordChangeParameters](docs/RequestPasswordChangeParameters.md)
 - [RequestSepaDirectDebitParams](docs/RequestSepaDirectDebitParams.md)
 - [RequestSepaMoneyTransferParams](docs/RequestSepaMoneyTransferParams.md)
 - [Security](docs/Security.md)
 - [SecurityList](docs/SecurityList.md)
 - [SingleDirectDebitData](docs/SingleDirectDebitData.md)
 - [SingleMoneyTransferRecipientData](docs/SingleMoneyTransferRecipientData.md)
 - [SplitTransactionsParams](docs/SplitTransactionsParams.md)
 - [SubTransactionParams](docs/SubTransactionParams.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionList](docs/TransactionList.md)
 - [TriggerCategorizationParams](docs/TriggerCategorizationParams.md)
 - [TwoStepProcedure](docs/TwoStepProcedure.md)
 - [UpdateBankConnectionParams](docs/UpdateBankConnectionParams.md)
 - [UpdateMultipleTransactionsParams](docs/UpdateMultipleTransactionsParams.md)
 - [UpdateResult](docs/UpdateResult.md)
 - [UpdateTransactionsParams](docs/UpdateTransactionsParams.md)
 - [User](docs/User.md)
 - [UserCreateParamsImpl](docs/UserCreateParamsImpl.md)
 - [UserIdentifiersList](docs/UserIdentifiersList.md)
 - [UserIdentifiersParams](docs/UserIdentifiersParams.md)
 - [UserInfo](docs/UserInfo.md)
 - [UserUpdateParamsImpl](docs/UserUpdateParamsImpl.md)
 - [VerificationStatusResource](docs/VerificationStatusResource.md)


## Documentation For Authorization


## finapi_auth

- **Type**: OAuth
- **Flow**: accessCode
- **Authorization URL**: /oauth/authorize
- **Scopes**: 
 - **all**: modify any sources


## Author



