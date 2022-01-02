-- data test
-- select c.CountyName, count(*) from staging.stg_county c GROUP by  c.CountyName, c.statename having count(*) > 1

-- with
--     county
--     as
--     (
--         SELECT
--             c.county county,
--             c.state state
--         FROM  c
--     GROUP BY county, "state"
    
    
-- )

--perhaps revisit the method of creating this model

with
    county
    as
    (
        SELECT
            c.county county,
            c.state "state",
            sa."Postal_Abbreviation" StateAbrv
        FROM {{source("public", "County")}} c
        INNER JOIN public."StateAbbreviations" sa on c."state" = sa."Us_State"
    GROUP BY county, "state", sa."Postal_Abbreviation"
    UNION
    select
        b.county county,
        sa."Us_State" "state",
        b."location state" StateAbrv       
    FROM {{source("public", "Business")}} b
    LEFT JOIN public."StateAbbreviations" sa on b."location state" = sa."Postal_Abbreviation"
    group by county, sa."Us_State", b."location state"    
)

-- if the stateabbrv has no corresponding statename we will keep the stateabbrv as the statename
select 
    ROW_NUMBER() OVER(order by county DESC) CountyID,
    county CountyName,
    case 
    when "state" is null then StateAbrv
    else "state"
    end as StateName,
    cast(now() as timestamp(3) without time zone) LastEditedWhen
from county 