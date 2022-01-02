
with
    category
    as
    (
        select
            row_number() OVER (order by c.title) CategoryID,
            c.title CategoryName 
        from {{ source("public", "Categories") }} c
        GROUP BY c.title
    )
    

select CategoryID, replace(categoryname, '"', '') as CategoryName, cast(now() as timestamp(3) without time zone) as LastEditedWhen
from category