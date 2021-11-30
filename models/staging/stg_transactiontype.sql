

with distinct_transactions as (
    select 
        DISTINCT [transaction] [transaction]
    FROM {{source("dbo", "Transactions")}}
)

select 
ROW_NUMBER() OVER(order by [transaction]) [TransactionID],
[transaction] [TransactionName],
GETDATE() LastEditedWhen
from distinct_transactions