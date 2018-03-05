# Security

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Identifier. Note: Whenever a security account is being updated, its security positions will be internally re-created, meaning that the identifier of a security position might change over time. | 
**account_id** | **int** | Security account identifier | 
**name** | **str** | Name | [optional] 
**isin** | **str** | ISIN | [optional] 
**wkn** | **str** | WKN | [optional] 
**quote** | **float** | Quote | [optional] 
**quote_currency** | **str** | Currency of quote | [optional] 
**quote_type** | **str** | Type of quote. &#39;PERC&#39; if quote is a percentage value, &#39;ACTU&#39; if quote is the actual amount | [optional] 
**quote_date** | **str** | Quote date | [optional] 
**quantity_nominal** | **float** | Value of quantity or nominal | [optional] 
**quantity_nominal_type** | **str** | Type of quantity or nominal value. &#39;UNIT&#39; if value is a quantity, &#39;FAMT&#39; if value is the nominal amount | [optional] 
**market_value** | **float** | Market value | [optional] 
**market_value_currency** | **str** | Currency of market value | [optional] 
**entry_quote** | **float** | Entry quote | [optional] 
**entry_quote_currency** | **str** | Currency of entry quote | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


