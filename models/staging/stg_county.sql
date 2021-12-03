-- data test
-- select c.CountyName, count(*) from staging.stg_county c GROUP by  c.CountyName, c.statename having count(*) > 1

with
    county
    as
    (
        SELECT
            c.county county,
            c.state state
        FROM {{source("dbo", "County")}} c
    GROUP BY county, [state]
    
    
)

SELECT
    ROW_NUMBER() OVER(order by county DESC) CountyID,
    county CountyName,
    [state] StateName,
    GETDATE() LastEditedWhen
FROM county