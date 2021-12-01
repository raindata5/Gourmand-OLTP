

with
    county
    as
    (
        SELECT
            c.county county
        FROM {{source("dbo", "County")}} c
    GROUP BY county
    
)

SELECT
    ROW_NUMBER() OVER(order by county DESC) CountyID,
    county CountyName,
    GETDATE() LastEditedWhen
FROM county