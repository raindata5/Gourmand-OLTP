

with distinct_transactions as (
    select 
        DISTINCT "transaction" transaction
    FROM {{source("public", "Transactions")}}
)

select 
ROW_NUMBER() OVER(order by "transaction") TransactionID,
"transaction" TransactionName,
cast(now() as timestamp(3) without time zone) LastEditedWhen
from distinct_transactions