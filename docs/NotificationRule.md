# NotificationRule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Notification rule identifier | 
**trigger_event** | **str** | Trigger event type | 
**params** | **dict(str, str)** | Additional parameters that are specific to the trigger event type. Please refer to the documentation for details. | [optional] 
**callback_handle** | **str** | The string that finAPI includes into the notifications that it sends based on this rule. | [optional] 
**include_details** | **bool** | Whether the notification messages that will be send based on this rule contain encrypted detailed data or not | [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


