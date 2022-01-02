with
    Countries
    as
    (
        SELECT
            *
        FROM {{ ref("stg_country") }}
    )

select * from Countries