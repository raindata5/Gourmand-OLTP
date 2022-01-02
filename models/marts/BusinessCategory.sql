
with
    category
    as
    (
        select
            *
        from {{ ref("stg_businesscategory") }}
    )
    

select *
from category