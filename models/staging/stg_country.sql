with
    Countries
    as
    (
        SELECT
            SELECT 
            DISTINCT b.[location country] Country
        from {{source("dbo", "Business")}}
    )
,
SELECT 
    ROW_NUMBER() OVER (order BY StateName) CountryID,
    Country CountryName
FROM Countries