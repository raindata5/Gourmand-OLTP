
-- considered
with
    counties1
    as
    (
        -- SELECT
        --     c.CountyName ,
        --     c.StateName ,
        --     sa.Postal_Abbreviation AbrvState,
        --     b."location country" Country
    select 
        c.CountyName ,
        c.StateName ,
        case
        when sa."Postal_Abbreviation" is null then c.StateName
        else sa."Postal_Abbreviation"
        end as AbrvState
    from {{ref("stg_county")}} c 
    LEFT JOIN {{source("public", "StateAbbreviations")}} sa on c.StateName = sa."Us_State"
    

),
counties2 as (
    select 
        c1.CountyName,
        c1.StateName,
        c1.AbrvState,
        b."location country" Country
    from counties1 c1
    LEFT JOIN {{source("public", "Business")}} b on c1.CountyName = b.county and AbrvState=b."location state"
),
countyish as
(   SELECT
    distinct StateName,
    AbrvState,
    Country
from counties2
where Country is not null
-- otherwise if there are null there will be duplicates when considering StateName, or AbrvState
),
countyish2 as
(
SELECT
-- this dense ranks forces the force state in each group to either have a null
-- assuming it's the sole member or a state abreviation assuming it's part of a group
-- this mostly does the same as the preceding "where Country is not null"
-- however this while this row_number can be skipped the preceding SARG can't be since even
-- states with null values would be included
-- either way I don't have to worry about nulls in abrv state
    ROW_NUMBER() OVER (PARTITION BY StateName ORDER BY Country DESC) stategroup,
    StateName,
    AbrvState,
    Country
FROM countyish
)

SELECT
    ROW_NUMBER() OVER (order BY StateName) StateID,
    case 
    when c2.StateName = '' then 'Unknown'
    else c2.StateName
    end as StateName,
    case 
    when c2.AbrvState = '' then 'Unknown'
    else c2.AbrvState
    end as AbrvState
    ,
    c.CountryID CountryID,   
    cast(now() as timestamp(3) without time zone) LastEditedWhen
FROM countyish2 c2
left join {{ref("stg_country")}} c on c2.Country=c.CountryName
where c2.stategroup = 1