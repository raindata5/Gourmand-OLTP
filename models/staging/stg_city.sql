with full_location as (
        select 
        b."location city" CityName,
        b."location state" StateAbrv,
        b.county County
    FROM {{source("public", "Business")}} b
),

normalized_loc as (
    SELECT
        fl.CityName,
        ss.StateID,
        sc.CountyID,
        sc.CountyName,
        ss.AbrvState
    FROM full_location fl
    -- ignore
    -- some of these businesses seem to have faulty state abbreviations e.g. London ,Laurel County XGL (kentucky)
    -- I will allow a script to run so that these can be filtered out and further processes
    LEFT JOIN {{ref("stg_state")}} ss on fl.StateAbrv=ss.AbrvState
    LEFT JOIN {{ref("stg_county")}} sc on fl.County = sc.CountyName and ss.StateName=sc.StateName
)

select
    ROW_NUMBER() OVER (order by nl.CityName) CityID,
    nl.CityName,
    nl.StateID,
    nl.CountyID,
    cast(now() as timestamp(3) without time zone) LastEditedWhen
from normalized_loc nl
GROUP BY nl.CityName, nl.StateID, nl.CountyID




-- getting the bad business loc records
-- with full_location as (
--         select 
--         b."location city" CityName,
--         b."location state" StateAbrv,
--         b.county County
--     FROM "GourmandOLTP"."public"."Business" b
    
-- )
--     SELECT
--         fl.*
--         -- fl.CityName,
--         -- ss.StateID,
--         -- sc.CountyID,
--         -- sc.CountyName,
--         -- ss.AbrvState
--     FROM full_location fl
--     WHERE not exists (
--         select 1 
--         from "GourmandOLTP"."_Staging"."stg_state" ss
--         where ss.AbrvState = fl.StateAbrv
-- )



-- for those where neither the county or statename correspond to one in the census
-- with full_location as (
--         select 
--         b."location city" CityName,
--         b."location state" StateAbrv,
--         b.county County
--     FROM "GourmandOLTP"."public"."Business" b
    
-- )


-- SELECT
--     fl.CityName,
--     ss.StateID,
--     sc.CountyID,
--     sc.CountyName,
--     ss.AbrvState,
--     fl.County
-- FROM full_location fl
-- inner JOIN "GourmandOLTP"."_Staging"."stg_state" ss on fl.StateAbrv=ss.AbrvState
-- LEFT JOIN "GourmandOLTP"."_Staging"."stg_county" sc on fl.County = sc.CountyName and ss.StateName=sc.StateName
-- WHERE sc.CountyID is null or sc.CountyName is null