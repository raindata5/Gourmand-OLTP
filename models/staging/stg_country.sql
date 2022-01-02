with
    Countries
    as
    (
        SELECT 
            DISTINCT b."location country" Country
        from {{source("public", "Business")}} b
    )
SELECT 
    ROW_NUMBER() OVER (order BY Country) CountryID,
    Country CountryName,
    cast(now() as timestamp(3) without time zone) LastEditedWhen
FROM Countries