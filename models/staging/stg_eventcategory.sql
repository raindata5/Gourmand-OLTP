with categories_cte as
( 
    SELECT
    e.category
from {{source("public", "Event")}} e
GROUP by e.category
)

select 
    ROW_NUMBER() OVER(order by c.category) EventCategoryID,
    c.category EventCategoryName,
    cast(now() as timestamp(3) without time zone) LastEditedWhen
FROM categories_cte c