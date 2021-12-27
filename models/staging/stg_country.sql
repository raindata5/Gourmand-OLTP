with
    Countries
    as
    (
        SELECT 
            DISTINCT b.[location country] Country
        from {{source("dbo", "Business")}} b
    )
SELECT 
    ROW_NUMBER() OVER (order BY Country) CountryID,
    Country CountryName,
    GETDATE() LastEditedWhen
FROM Countries