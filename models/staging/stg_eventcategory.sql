with categories_cte as
( 
    SELECT
    e.category
from {{source("dbo", "Event")}} e
GROUP by e.category
)

select 
    ROW_NUMBER() OVER(order by c.category) EventCategoryID,
    c.category EventCategoryName
FROM categories_cte c