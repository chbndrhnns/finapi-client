# BankConnection

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Bank connection identifier | 
**bank_id** | **int** | Identifier of the bank that this connection belongs to. NOTE: This field is DEPRECATED and will get removed at some point. Please refer to the &#39;bank&#39; field instead. | 
**bank** | [**Bank**](Bank.md) | Bank that this connection belongs to | 
**name** | **str** | Custom name for the bank connection. You can set this field with the &#39;Edit a bank connection&#39; service, as well as during the initial import of the bank connection. Maximum length is 64. | [optional] 
**banking_user_id** | **str** | Stored online banking user ID credential. This field may be null for the &#39;demo connection&#39;. | [optional] 
**banking_customer_id** | **str** | Stored online banking customer ID credential | [optional] 
**banking_pin** | **str** | Stored online banking PIN. Note that each symbol of the PIN is distorted with an &#39;X&#39; character. | [optional] 
**type** | **str** | Bank connection type | 
**update_status** | **str** | Current status of transactions download. The POST /bankConnections/import and POST /bankConnections/&lt;id&gt;/update services will set this flag to IN_PROGRESS before they return. Once the import or update has finished, the status will be changed to READY. | 
**categorization_status** | **str** | Current status of transactions categorization. The asynchronous download process that is triggered by a call of the POST /bankConnections/import and POST /bankConnections/&lt;id&gt;/update services (and also by finAPI&#39;s auto update, if enabled) will set this flag to PENDING once the download has finished and a categorization is scheduled for the imported transactions. A separate categorization thread will then start to categorize the transactions (during this process, the status is IN_PROGRESS). When categorization has finished, the status will be (re-)set to READY. Note that the current categorization status should only be queried after the download has finished, i.e. once the download status has switched from IN_PROGRESS to READY. | 
**last_manual_update** | [**UpdateResult**](UpdateResult.md) | Result of the last manual update of this bank connection. If no manual update has ever been done so far, then this field will not be set. | [optional] 
**last_auto_update** | [**UpdateResult**](UpdateResult.md) | Result of the last auto update of this bank connection (ran by finAPI&#39;s automatic batch update process). If no auto update has ever been done so far, then this field will not be set. | [optional] 
**two_step_procedures** | [**list[TwoStepProcedure]**](TwoStepProcedure.md) | Available two-step-procedures for this bank connection, used for submitting a money transfer or direct debit request (see /accounts/requestSepaMoneyTransfer or /requestSepaDirectDebit). The available two-step-procedures are re-evaluated each time this bank connection is updated (/bankConnections/update). This means that this list may change as a result of an update. | [optional] 
**iban_only_money_transfer_supported** | **bool** | Whether this bank connection accepts money transfer requests where the recipient&#39;s account is defined just by the IBAN (without an additional BIC). This field is re-evaluated each time this bank connection is updated. See also: /accounts/requestSepaMoneyTransfer | [default to False]
**iban_only_direct_debit_supported** | **bool** | Whether this bank connection accepts direct debit requests where the debitor&#39;s account is defined just by the IBAN (without an additional BIC). This field is re-evaluated each time this bank connection is updated. See also: /accounts/requestSepaDirectDebit | [default to False]
**collective_money_transfer_supported** | **bool** | &lt;b&gt;DEPRECATED! DO NOT USE THIS FIELD, AS IT IS UNRELIABLE. INSTEAD, REFER TO THE &#39;supportedOrders&#39; FIELD IN THE ACCOUNT RESOURCE.&lt;/b&gt;&lt;br/&gt;&lt;br/&gt;Whether this bank connection supports submitting collective money transfers. This field is re-evaluated each time this bank connection is updated. See also: /accounts/requestSepaMoneyTransfer | [default to False]
**default_two_step_procedure_id** | **str** | The default two-step-procedure. Must match one of the available &#39;procedureId&#39;s from the &#39;twoStepProcedures&#39; list. When this field is set, you can execute two-step-procedures (accounts/requestSepaMoneyTransfer or /requestSepaDirectDebit) without having to explicitly set a procedure. finAPI will use the default procedure in such cases. Note that the list of available procedures of a bank connection may change as a result of an update of the connection, and if this field references a procedure that is no longer available after an update, finAPI will automatically clear the default procedure (set it to null). | [optional] 
**account_ids** | **list[int]** | Identifiers of the accounts that belong to this bank connection | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


