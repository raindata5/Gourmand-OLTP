-- attempt to add some sort of updated_at column

with
    cats
    as
    (
        SELECT 
            *
        from {{ref("stg_eventcategory")}}
    )

SELECT 
    * 
from cats