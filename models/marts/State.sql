with
    States
    as
    (
        SELECT 
            *
        from {{ref("stg_state")}}
    )

SELECT 
    * 
from States
