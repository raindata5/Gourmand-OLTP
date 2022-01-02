{% set levels2 = [[1, "$"],[2, "$$"],[3, "$$$"],[4, "$$$$"]] %}

with
    stg_business_dbt
    as
    (
        SELECT
            BusinessID,
            BusinessName,
            ChainName,
            CASE AddressLine1
        when '' THEN null 
        else AddressLine1
        end as AddressLine1,
            CASE AddressLine2
        when '' THEN null 
        else AddressLine2
        end as AddressLine2,
            CASE AddressLine3
        when '' THEN null 
        else AddressLine3
        end as AddressLine3,
            Latitude,
            Longitude,
            ZipCode,
            CountryName,
            AbrvState,
            BusinessPhone,
            BusinessURL,
            CASE BusinessStatus
        when 'False' THEN 0 
        else 1
        end as is_closed,
            Rating,
            ReviewCount,
            DistanceToCounty,
            CityName,
            CASE
            {%- for level in levels2 %}
            when length(price) = '{{ level[0] }}' then '{{ level[1] }}'
            {% endfor -%}
            ELSE 'Unknown'
            END as price,
            county,
            DateSurveyed
        FROM {{ref("stg_business")}}
), bus_norm as
(


select
    sb.BusinessID,
    sb.BusinessName,
    sb.ChainName,
    sb.AddressLine1,
    sb.AddressLine2,
    sb.AddressLine3,
    sb.Latitude,
    sb.Longitude,
    sb.ZipCode,
    sb.BusinessPhone,
    sb.BusinessURL,
    sb.is_closed,
    sb.DistanceToCounty,
    sc.CityID,
    sc.CountyID,
    sc.StateID,
    pl.PaymentLevelID,
    cast(now() as timestamp(3) without time zone) LastEditedWhen


FROM stg_business_dbt sb
INNER JOIN {{ref("PaymentLevel")}} pl on sb.price = pl.PaymentLevelSymbol
INNER JOIN {{ref("State")}} s on sb.AbrvState = s.AbrvState
INNER JOIN {{ref("County")}} c on sb.county = c.CountyName and s.StateID = c.StateID
INNER JOIN {{ref("City")}} sc on sb.CityName = sc.CityName and c.CountyID = sc.CountyID and s.StateID = sc.StateID
-- LEFT JOIN {{ref("stg_city")}} sc on sb.CityName = sc.CityName and c.CountyID = sc.CountyID and s.StateID = sc.StateID
)

SELECT
    *
FROM bus_norm