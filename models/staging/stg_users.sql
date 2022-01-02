--this dense rank is used to get the most up to date user info from the reviews we have
with most_recent_user as (
select 
ROW_NUMBER() OVER(PARTITION BY "user id" order by time_created desc) as user_history,
"user profile_url" UserProfileURL,
"user image_url" UserImageURL,
-- SUBSTRING("user name", 1, CHARINDEX(' ', "user name")) FirstName,
-- SUBSTRING("user name", CHARINDEX(' ', "user name"), CHARINDEX('.', "user name") - CHARINDEX(' ', "user name")) LastNameInitial
length("user name") - length(trim(right(trim("user name"), 2))) length_of_name,
trim(right(trim("user name"), 2)) initial,
"user name"
from {{ source("public", "Review") }}
)

select 
ROW_NUMBER() OVER(order by user_history) UserID,
UserProfileURL,
UserImageURL,
-- FirstName,
-- LastNameInitial,
    SUBSTRING("user name", 1, length_of_name) FirstName,
    initial LastNameInitial,
cast(now() as timestamp(3) without time zone) LastEditedWhen
from most_recent_user 
WHERE user_history = 1




-- with test as (
--     select 
-- DENSE_RANK() OVER(PARTITION BY "user id" order by time_created desc) as user_history,
-- "user profile_url" UserProfileURL,
-- "user image_url" UserImageURL,
-- SUBSTRING("user name", 1, CHARINDEX(' ', "user name")) FirstName,
-- SUBSTRING("user name", CHARINDEX(' ', "user name"), CHARINDEX('.', "user name") - CHARINDEX(' ', "user name")) LastNameInitial
-- from Review
-- )

-- select 
-- ROW_NUMBER() OVER(order by user_history) UserID,
-- UserProfileURL,
-- UserImageURL,
-- FirstName,
-- LastNameInitial,
-- cast(now() as timestamp(3) without time zone) LastEditedWhen
-- from test 
-- WHERE user_history = 1