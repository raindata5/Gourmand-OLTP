
with most_recent_user as (
select 
DENSE_RANK() OVER(PARTITION BY [user id] order by time_created desc) as user_history,
[user profile_url] UserProfileURL,
[user image_url] UserImageURL,
SUBSTRING([user name], 1, CHARINDEX(' ', [user name])) FirstName,
SUBSTRING([user name], CHARINDEX(' ', [user name]), CHARINDEX('.', [user name]) - CHARINDEX(' ', [user name])) LastNameInitial
from {{ source("dbo", "Review") }}
)

select 
ROW_NUMBER() OVER(order by user_history) UserID,
UserProfileURL,
UserImageURL,
FirstName,
LastNameInitial,
GETDATE() LastEditedWhen
from most_recent_user 
WHERE user_history = 1




-- with test as (
--     select 
-- DENSE_RANK() OVER(PARTITION BY [user id] order by time_created desc) as user_history,
-- [user profile_url] UserProfileURL,
-- [user image_url] UserImageURL,
-- SUBSTRING([user name], 1, CHARINDEX(' ', [user name])) FirstName,
-- SUBSTRING([user name], CHARINDEX(' ', [user name]), CHARINDEX('.', [user name]) - CHARINDEX(' ', [user name])) LastNameInitial
-- from Review
-- )

-- select 
-- ROW_NUMBER() OVER(order by user_history) UserID,
-- UserProfileURL,
-- UserImageURL,
-- FirstName,
-- LastNameInitial,
-- GETDATE() LastEditedWhen
-- from test 
-- WHERE user_history = 1