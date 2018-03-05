# EditBankConnectionParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**banking_user_id** | **str** | New online banking user ID. If you do not want to change the current user ID let this field remain unset. Note that you cannot clear the current user ID, i.e. a bank connection must always have a user ID (except for when it is a &#39;demo connection&#39;). Max length: 64. | [optional] 
**banking_customer_id** | **str** | New online banking customer ID. If you do not want to change the current customer ID let this field remain unset. If you want to clear the current customer ID, set the field&#39;s value to an empty string (\&quot;\&quot;). Max length: 64. | [optional] 
**banking_pin** | **str** | New online banking PIN. If you do not want to change the current PIN let this field remain unset. If you want to clear the current PIN, set the field&#39;s value to an empty string (\&quot;\&quot;).&lt;br/&gt;&lt;br/&gt;NOTE: Before you set this field, please regard the &#39;pinsAreVolatile&#39; flag of this connection&#39;s bank. Any symbols are allowed. Max length: 170. | [optional] 
**default_two_step_procedure_id** | **str** | New default two-step-procedure. Must match the &#39;procedureId&#39; of one of the procedures that are listed in the bank connection. If you do not want to change this field let it remain unset. If you want to clear the current default two-step-procedure, set the field&#39;s value to an empty string (\&quot;\&quot;). | [optional] 
**name** | **str** | New name for the bank connection. Maximum length is 64. If you do not want to change the current name let this field remain unset. If you want to clear the current name, set the field&#39;s value to an empty string (\&quot;\&quot;). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


