# RequestSepaMoneyTransferParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recipient_name** | **str** | Name of the recipient. Note: Neither finAPI nor the involved bank servers are guaranteed to validate the recipient name. Even if the recipient name does not depict the actual registered account holder of the specified recipient account, the money transfer request might still be successful. This field is optional only when you pass a clearing account as the recipient. Otherwise, this field is required. | [optional] 
**recipient_iban** | **str** | IBAN of the recipient&#39;s account. This field is optional only when you pass a clearing account as the recipient. Otherwise, this field is required. | [optional] 
**recipient_bic** | **str** | BIC of the recipient&#39;s account. Note: This field is optional when you pass a clearing account as the recipient or if the bank connection of the account that you want to transfer money from supports the IBAN-Only money transfer. You can find this out via GET /bankConnections/&lt;id&gt;. Also note that when a BIC is given, then this BIC will be used for the money transfer request independent of whether it is required or not (unless you pass a clearing account, in which case this field will always be ignored). | [optional] 
**clearing_account_id** | **str** | Identifier of a clearing account. If this field is set, then the fields &#39;recipientName&#39;, &#39;recipientIban&#39; and &#39;recipientBic&#39; will be ignored and the recipient account will be the specified clearing account. | [optional] 
**amount** | **float** | The amount to transfer. Must be a positive decimal number with at most two decimal places (e.g. 99.90) | 
**purpose** | **str** | The purpose of the transfer transaction | [optional] 
**account_id** | **int** | Identifier of the bank account that you want to transfer money from | 
**banking_pin** | **str** | Online banking PIN. If a PIN is stored in the account&#39;s bank connection, then this field may remain unset. If the field is set though then it will always be used (even if there is some other PIN stored in the bank connection). | [optional] 
**two_step_procedure_id** | **str** | The bank-given ID of the two-step-procedure that should be used for the money transfer. For a list of available two-step-procedures, see the corresponding bank connection (GET /bankConnections). If this field is not set, then the bank connection&#39;s default two-step procedure will be used. Note that in this case, when the bank connection has no default two-step procedure set, then the service will return an error (see response messages for details). | [optional] 
**challenge_response** | **str** | Challenge response. This field should be set only when the previous attempt to request a SEPA money transfer failed with HTTP code 510, i.e. the bank sent a challenge for the user for an additional authentication. In this case, this field must contain the response to the bank&#39;s challenge. | [optional] 
**additional_money_transfers** | [**list[SingleMoneyTransferRecipientData]**](SingleMoneyTransferRecipientData.md) | In case that you want to submit not just a single money transfer, but do a collective money transfer, use this field to pass a list of additional money transfer orders. The service will then pass a collective money transfer request to the bank, including both the money transfer specified on the top-level, as well as all money transfers specified in this list. Note that you should check the account&#39;s &#39;supportedOrders&#39; field to find out whether or not it is supporting collective money transfers. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


