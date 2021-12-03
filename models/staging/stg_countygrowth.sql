

with initial_county_growth as (
    SELECT
        c.county CountyName,
        stg_c.statename,
        c.[year] GrowthYear,
        c.POP EstimatedPopulation,
        stg_c.CountyID CountyID
    FROM {{source("dbo", "County")}} c
    left JOIN {{ref("stg_county")}} stg_c on c.county = stg_c.CountyName and c.[state]= stg_c.statename
),

country_growth_with_c_id as (
    SELECT
        g.CountyID,
        g.GrowthYear EstimationYear,
        -- stg_s.StateID,
        g.EstimatedPopulation,
        GETDATE() LastEditedWhen
    FROM initial_county_growth g
    -- LEFT JOIN {{ref("stg_state")}} stg_s on g.statename = stg_s.statename
)

SELECT 
*
FROM country_growth_with_c_id