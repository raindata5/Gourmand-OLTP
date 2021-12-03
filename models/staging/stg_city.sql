with full_location as (
        select 
        b.[location city] CityName,
        b.[location state] StateAbrv,
        b.county County
    FROM {{source("dbo", "Business")}} b
),

normalized_loc as (
    SELECT
        fl.CityName,
        ss.StateID,
        sc.CountyID,
        sc.CountyName,
        ss.AbrvState
    FROM full_location fl
    LEFT JOIN {{ref("stg_state")}} ss on fl.StateAbrv=ss.AbrvState
    LEFT JOIN {{ref("stg_county")}} sc on fl.County = sc.CountyName and ss.StateName=sc.StateName
)

select
    ROW_NUMBER() OVER (order by nl.CityName) CityID,
    nl.CityName,
    nl.StateID,
    nl.CountyID,
    getdate() LastEditedWhen
from normalized_loc nl
GROUP BY nl.CityName, nl.StateID, nl.CountyID