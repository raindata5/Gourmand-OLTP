with reviews as (
    SELECT
        *
    FROM {{ref("stg_review")}}
)

select * from reviews