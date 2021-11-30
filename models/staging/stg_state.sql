

with
    counties
    as
    (
        SELECT
            c.county CountyName,
            c.[state] StateName,
            b.[location state] AbrvState,
            b.[location country] Country
        from {{source("dbo", "Business")}} b
  RIGHT JOIN {{source("dbo", "County")}} c on b.county = c.county
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
    DENSE_RANK() OVER (PARTITION BY StateName ORDER BY AbrvState DESC) stategroup,
    StateName,
    AbrvState.
    Country
FROM countyish
)

SELECT
    ROW_NUMBER() OVER (order BY StateName) StateID,
    StateName,
    AbrvState,
    Country CountryName,
    GETDATE() LastEditedWhen
FROM countyish2
WHERE stategroup = 1