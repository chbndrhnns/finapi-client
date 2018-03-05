# RequestSepaDirectDebitParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **int** | Identifier of the bank account to which you want to transfer the money. | 
**banking_pin** | **str** | Online banking PIN. If a PIN is stored in the account&#39;s bank connection, then this field may remain unset. If the field is set though then it will always be used (even if there is some other PIN stored in the bank connection). | [optional] 
**two_step_procedure_id** | **str** | The bank-given ID of the two-step-procedure that should be used for the direct debit order. For a list of available two-step-procedures, see the corresponding bank connection (GET /bankConnections). If this field is not set, then the bank connection&#39;s default two-step procedure will be used. Note that in this case, when the bank connection has no default two-step procedure set, then the service will return an error (see response messages for details). | [optional] 
**direct_debit_type** | **str** | Type of the direct debit; either &lt;code&gt;BASIC&lt;/code&gt; or &lt;code&gt;B2B&lt;/code&gt; (Business-To-Business). Please note that an account which supports the basic type must not necessarily support B2B (or vice versa). Check the source account&#39;s &#39;supportedOrders&#39; field to find out which types of direct debit it supports.&lt;br/&gt;&lt;br/&gt; | 
**sequence_type** | **str** | Sequence type of the direct debit. Possible values:&lt;br/&gt;&lt;br/&gt;&amp;bull; &lt;code&gt;OOFF&lt;/code&gt; - means that this is a one-time direct debit order&lt;br/&gt;&amp;bull; &lt;code&gt;FRST&lt;/code&gt; - means that this is the first in a row of multiple direct debit orders&lt;br/&gt;&amp;bull; &lt;code&gt;RCUR&lt;/code&gt; - means that this is one (but not the first or final) within a row of multiple direct debit orders&lt;br/&gt;&amp;bull; &lt;code&gt;FNAL&lt;/code&gt; - means that this is the final in a row of multiple direct debit orders&lt;br/&gt;&lt;br/&gt; | 
**execution_date** | **str** | Execution date for the direct debit(s), in the format &#39;yyyy-MM-dd&#39;. | 
**direct_debits** | [**list[SingleDirectDebitData]**](SingleDirectDebitData.md) | List of the direct debits that you want to execute. Please check the account&#39;s &#39;supportedOrders&#39; field to find out whether you can pass multiple direct debits or just one. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


