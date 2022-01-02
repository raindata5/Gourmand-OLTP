with stg_event as (
    select 
         EventID,
         BusinessID,
         EventName,
         Attending,
         Cost CostOfAttending,
         Free is_free,
         EventDescription,
         Interested,
         CityID,
         latitude,
         longitude,
         ZipCode,
         StartTime,
         EndTime,
         TicketsUrl,
         EventSiteUrl,
         CancelDate,
         OfficialDate,
         CreatedAt,
         LastEditedWhen
    from {{ref("stg_event")}}
)
SELECT
    *
FROM stg_event