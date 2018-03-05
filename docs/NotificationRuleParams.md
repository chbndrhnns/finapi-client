# NotificationRuleParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_event** | **str** | Trigger event type | 
**params** | **dict(str, str)** | Additional parameters that are specific to the chosen trigger event type. Please refer to the documentation for details. | [optional] 
**callback_handle** | **str** | An arbitrary string that finAPI will include into the notifications that it sends based on this rule and that you can use to identify the notification in your application. For instance, you could include the identifier of the user that you create this rule for. Maximum allowed length of the string is 512 characters.&lt;br/&gt;&lt;br/&gt;Note that for this parameter, you can pass the symbols &#39;/&#39;, &#39;&#x3D;&#39;, &#39;%&#39; and &#39;\&quot;&#39; in addition to the symbols that are generally allowed in finAPI (see https://finapi.zendesk.com/hc/en-us/articles/222013148). This was done to enable you to set Base64 encoded strings and JSON structures for the callback handle. | [optional] 
**include_details** | **bool** | Whether the notification messages that will be send based on this rule should contain encrypted detailed data or not | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


