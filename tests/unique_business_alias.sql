select * 
from {{ref("stg_business")}}
WHERE EXISTS (
    select 1 
    FROM {{ref("stg_business")}}
    group by BusinessID
    having count(*) > 1
) 