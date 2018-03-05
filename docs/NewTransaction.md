# NewTransaction

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount. Required. | 
**purpose** | **str** | Purpose. Any symbols are allowed. Maximum length is 2000. Optional. Default value: null. | [optional] 
**counterpart** | **str** | Counterpart. Any symbols are allowed. Maximum length is 80. Optional. Default value: null. | [optional] 
**counterpart_iban** | **str** | Counterpart IBAN. Optional. Default value: null. | [optional] 
**counterpart_blz** | **str** | Counterpart BLZ. Optional. Default value: null. | [optional] 
**counterpart_bic** | **str** | Counterpart BIC. Optional. Default value: null. | [optional] 
**booking_date** | **str** | Booking date in the format &#39;yyyy-MM-dd&#39;.&lt;br/&gt;&lt;br/&gt;If the date lies back more than 10 days from the booking date of the latest transaction that currently exists in the account, then this transaction will be ignored and not imported. If the date depicts a date in the future, then finAPI will deal with it the same way as it does with real transactions during a real update (see fields &#39;bankBookingDate&#39; and &#39;finapiBookingDate&#39; in the Transaction Resource for explanation).&lt;br/&gt;&lt;br/&gt;This field is optional, default value is the current date. | [optional] 
**value_date** | **str** | Value date in the format &#39;yyyy-MM-dd&#39;. Optional. Default value: Same as the booking date. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


