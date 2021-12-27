
with
    category
    as
    (
        select
            row_number() OVER (order by c.title) CategoryID,
            c.title CategoryName 
        from {{ source("dbo", "Categories") }} c
        GROUP BY c.title
    )
    

select CategoryID, replace(categoryname, '"', '') as CategoryName, GETDATE() as LastEditedWhen
from category