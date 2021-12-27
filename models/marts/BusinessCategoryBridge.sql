with bcb as (
    SELECT 
        *
    FROM {{ref("stg_businesscategorybridge")}}
)

select 
    *
from bcb