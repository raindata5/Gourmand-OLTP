{{ config(schema='Analytics') }}

with
    c_growth
    as
    (
        SELECT 
            *
        from {{ ref("stg_countygrowth") }}
    )

SELECT 
    * 
from c_growth