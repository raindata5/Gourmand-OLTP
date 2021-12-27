with stock as (
    SELECT
        row_number() OVER(ORDER BY b.DateSurveyed, b.BusinessID) BusinessHoldingID,
        b.BusinessID,
        b.Rating BusinessRating,
        b.ReviewCount,
        b.DateSurveyed CloseDate
    FROM {{ref("stg_business")}} b
)

select *
from stock