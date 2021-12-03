
with
    transactions
    as
    (
        select
            *
        from {{ ref("stg_transactiontype") }} 
    )
    

select *
from transactions