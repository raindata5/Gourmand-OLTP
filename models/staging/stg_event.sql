 -- will attempt to implement accumulating snapshot fact table
 -- duplicates were already removed but could do my previous dense rank method
-- using order by for columns that would generally not be null until a later date
with first_event as (
    SELECT
        e.business_id BusinessName,
        e.attending_count Attending,
-- cost was showing up as blanks without nulls
        case e.cost
        when '' then 0.0
        else cast(e.cost as numeric(15,0))
        end as Cost,
        replace(e.[description],'\n','') EventDescription,
        e.interested_count Interested,
		case e.latitude
		when '' then NULL
		else e.latitude
		end as Latitude,
		case e.longitude
		when '' then NULL
		else e.longitude
		end as Longitude,
-- offset due to ISO 8601 being used
        CAST(e.time_start as datetimeoffset) StartTime,
        CASE e.time_end 
        when '' then null
        else CAST(e.time_end as datetimeoffset)
        end as EndTime,
        CASE e.tickets_url
        when '' THEN null 
        else e.tickets_url
        end as TicketsURL,
        replace(e.[name],'\n','') EventName,
        e.event_site_url EventSiteURL,
        e.is_free Free,
-- going to make these null instead of false to implement
-- accumulating snapshot fact table further on down the line
-- since these extractions would be done daily this date will tell me
-- the day the change took place
        case e.is_canceled
        when 'False' then null
        else cast(e.time_extracted as date)
        end as CancelDate,
        case e.is_official
        when 'False' then null
        else cast(e.time_extracted as date)
        end as OfficialDate,
        cast(e.[location address1]as NVARCHAR(150)) AddressLine1,
        e.[location address2] AddressLine2,
        e.[location address3] AddressLine3,
        cast(e.[location city]as NVARCHAR(50)) CityName,
        e.[location zip_code] ZipCode,
        e.[location country] CountryName,
        e.[location state] AbrvState,
-- have to find a way to make sure this CreatedAt date stays static
        cast(e.time_extracted as date) CreatedAt,
        getdate() LastEditedWhen,
        e.category 
    FROM {{source("dbo","Event")}} e
),
normalized_event as (
    select
        ROW_NUMBER() OVER(order by fe.EventName) EventID,
        sb.BusinessID,
        fe.EventName,
        fe.Attending,
        fe.Cost,
        fe.EventDescription,
        fe.Interested,
        fe.Latitude,
        fe.Longitude,
        fe.StartTime,
        fe.EndTime,
        fe.TicketsURL,
        fe.EventSiteURL,
        fe.Free,
        fe.CancelDate,
        fe.OfficialDate,
        fe.AddressLine1,
        case fe.AddressLine2
        when '' then null 
        else fe.AddressLine2
        end as AddressLine2,
        case fe.AddressLine3
        when '' then null 
        else fe.AddressLine3
        end as AddressLine3,
        s_city.CityID,
        fe.ZipCode,
        s_country.CountryID,
        s_state.StateID,
        fe.CreatedAt,
        fe.LastEditedWhen
    from first_event fe
    left join {{ref("stg_business")}} sb on fe.BusinessName=sb.BusinessName
    left join {{ref("stg_eventcategory")}} ec on fe.category=ec.EventCategoryName
    left join {{ref("stg_state")}} s_state on fe.AbrvState=s_state.AbrvState
    left join {{ref("stg_county")}} s_county on sb.county=s_county.CountyName and s_state.StateName=s_county.statename
    left join {{ref("stg_city")}} s_city on fe.CityName=s_city.CityName and s_state.StateID=s_city.StateID and s_county.CountyID=s_city.CountyID
    left join {{ref("stg_country")}} s_country on fe.CountryName=s_country.CountryName
)
SELECT * from normalized_event