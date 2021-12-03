-- prefer to treat reviews as final since one can't redo a 
-- visit to a restaurant
with
    review_norm
    as
    (
        SELECT
            ROW_NUMBER() OVER(order by r.time_created) ReviewID,
            r.url ReviewURL,
            r.text ReviewExtract,
            r.rating ReviewRating,
            su.UserID,
            b.BusinessID,
            r.time_created CreatedAt,
            GETDATE() InsertedAt
        from {{ source("dbo", "Review") }} r
        INNER join {{ ref("stg_users") }} su on r.[user profile_url]=su.UserProfileURL
        LEFT JOIN {{ ref("stg_business") }} b on r.id = b.HRID

    )
select *
from review_norm