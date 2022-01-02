-- could possibly sitck with chain because I could concatenate and hash
-- together the categories hash it and then use that to decide  if
-- 2 business are apart of the same chain
with business as (
        SELECT
        ROW_NUMBER() OVER(PARTITION BY b.alias ORDER BY b.time_extracted DESC) MostRecentBusinessInfo, 
        cast(b.alias as text) BusinessName,
        cast(b.name as text) ChainName,
        cast(b."location address1"as text) AddressLine1,
        b."location address2" AddressLine2,
        b."location address3" AddressLine3,
        cast(b."location city"as text) CityName,
        b."location zip_code" ZipCode,
        b."location country" CountryName,
        b."location state" AbrvState,
        b.is_closed BusinessStatus,
        b.url BusinessURL,
        cast(CAST(review_count as numeric(15,0)) as int) ReviewCount,
        b.rating Rating,
        -- cast(SUBSTRING(b.phone, 1, CHARINDEX('.', b.phone, 1) -1 ) as text) BusinessPhone,
		b.display_phone BusinessPhone,
        cast(CAST(distance as numeric(15,0)) as int) DistanceToCounty,
		case "coordinates latitude"
		when '' then NULL
		else cast(b."coordinates latitude" as Decimal(8,6))
		end as Latitude,
		case "coordinates longitude"
		when '' then NULL
		else cast(b."coordinates longitude" as Decimal(9,6))
		end as Longitude,
        b.id HRID,
        b.county,
        b.price,
        cast(b.time_extracted as date) DateSurveyed

    from {{source("public", "Business")}} b 
),
create_bus_id as (
    select 
        DENSE_RANK() OVER(ORDER BY BusinessName) BusinessID,
        BusinessName,
        ChainName,
        AddressLine1,
        AddressLine2,
        AddressLine3,
        CityName,
        ZipCode,
        CountryName,
        AbrvState,
        BusinessStatus,
        BusinessURL,
        ReviewCount,
        Rating,
        BusinessPhone,
        DistanceToCounty,
        Latitude,
        Longitude,
        HRID,
        county,
        price,
        DateSurveyed

    from business 
    WHERE MostRecentBusinessInfo = 1
)
select *
from create_bus_id

-- WHERE EXISTS (
--     select 1 
--     FROM business
--     group by BusinessID
--     having count(*) > 1
-- ) 
-- data test