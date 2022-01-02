with bus_cat as (
    SELECT 
        b.BusinessID,
        c.title CategoryName
    from {{source("public", "Categories")}} c
    INNER JOIN {{ref("stg_business")}} b on c.businessalias=b.BusinessName
),
bus_cat_norm as (
    SELECT
        BusinessID,
        sc.CategoryID,
        cast(now() as timestamp(3) without time zone) LastEditedWhen
    FROM bus_cat bc
    INNER JOIN {{ref("stg_businesscategory")}} sc on bc.CategoryName=sc.CategoryName
)

select * from bus_cat_norm bcn