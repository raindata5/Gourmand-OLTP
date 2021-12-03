
-- considered
with
    counties
    as
    (
        SELECT
            c.CountyName ,
            c.StateName ,
            sa.Postal_Abbreviation AbrvState,
            b.[location country] Country
        from {{ref("stg_county")}} c 
        LEFT JOIN {{source("dbo", "StateAbbreviations")}} sa on c.StateName = sa.Us_State
        LEFT JOIN {{source("dbo", "Business")}} b on c.CountyName = b.county and sa.Postal_Abbreviation=b.[location state]

),
countyish as
(   SELECT
    distinct StateName,
    AbrvState,
    Country
from counties
)
,
countyish2 as
(
SELECT
-- this dense ranks forces the force state in each group to either have a null
-- assuming it's the sole member or a state abreviation assuming it's part of a group
-- revise this information
--essentially I don't have to worry about nulls in abrv state
    ROW_NUMBER() OVER (PARTITION BY StateName ORDER BY Country DESC) stategroup,
    StateName,
    AbrvState,
    Country
FROM countyish
)

SELECT
    ROW_NUMBER() OVER (order BY StateName) StateID,
    c2.StateName,
    c2.AbrvState,
    c.CountryID CountryID,   
    GETDATE() LastEditedWhen
FROM countyish2 c2
left join {{ref("stg_country")}} c on c2.Country=c.CountryName
where c2.stategroup = 1