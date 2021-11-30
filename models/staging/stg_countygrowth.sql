
-- select c.CountyName, count(*) from staging.stg_county c GROUP by  c.CountyName having count(*) > 1
-- add this as a test to counties

with initial_county_growth as (
    SELECT
        c.county CountyName,
        c.[year] GrowthYear,
        c.POP EstimatedPopulation,
        stg_c.CountyID CountyID
    FROM {{source("dbo", "County")}} c
    left JOIN {{ref("stg_county")}} stg_c on c.county = stg_c.CountyName
),

country_growth_with_c_id as (
    SELECT
        CountyID,
        GrowthYear,
        EstimatedPopulation,
        GETDATE() LastEditedWhen
    FROM initial_county_growth
)

SELECT 
*
FROM country_growth_with_c_id