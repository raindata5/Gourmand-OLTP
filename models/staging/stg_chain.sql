
with Chain as (
    Select
  ROW_NUMBER() OVER(order by name) ChainID,
  name  ChainName
from {{source("dbo", "Business")}}
group by name
)

select 
    ChainID,
    ChainName,
    GETDATE() as LastEditedWhen
from Chain