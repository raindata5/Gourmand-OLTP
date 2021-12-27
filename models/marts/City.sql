with
    cities
    as
    (
        SELECT 
            *
        from {{ref("stg_city")}}
    )

SELECT 
    * 
from cities