with
    business_tran
    as
    (
        SELECT 
            *
        from {{ref("stg_business_transaction_types")}}
    )

SELECT 
    * 
from business_tran