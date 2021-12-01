with business as (
        SELECT
        DENSE_RANK() OVER(ORDER BY b.alias) BusinessID, 
        cast(b.alias as NVARCHAR(100)) BusinessName,
        cast(b.name as NVARCHAR(100)) ChainName,
        cast(b.[location address1]as NVARCHAR(150)) AddressLine1,
        b.[location address2] AddressLine2,
        b.[location address3] AddressLine3,
        cast(b.[location city]as NVARCHAR(50)) CityName,
        b.[location zip_code] ZipCode,
        b.[location country] CountryName,
        b.[location state] AbrvState,
        b.is_closed BusinessStatus,
        b.url BusinessURL,
        cast(SUBSTRING(b.review_count, 1, CHARINDEX('.', b.review_count, 1) -1) as int) ReviewCount,
        b.rating Rating,
        cast(SUBSTRING(b.phone, 1, CHARINDEX('.', b.phone, 1) -1 ) as nvarchar(20)) BusinessPhone,
        cast(SUBSTRING(b.distance,1, CHARINDEX('.',b.distance,1) -1) as int) DistanceToCounty,
        cast(b.[coordinates latitude] as Decimal(8,6)) Latitude,
        cast(b.[coordinates longitude] as Decimal(9,6)) Longitude

    from {{source("dbo", "Business")}} b 
)

select * from business