
with
    category
    as
    (
        select
            *
        from {{ ref("stg_category") }}
    )
    

select *
from category