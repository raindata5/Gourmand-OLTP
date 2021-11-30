

with county as (
    SELECT
    county
    FROM {{source("dbo", "County")}}
    GROUP BY county
    
)

SELECT
ROW_NUMBER() OVER(order by county DESC) CountyID,
county CountyName,
GETDATE() LastEditedWhen
FROM county