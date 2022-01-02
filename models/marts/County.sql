-- check for uniqueness in county and state as a test

with
    county
    as
    (
        select
            c.CountyID,
            c.CountyName,
            s.StateID,
            c.LastEditedWhen
        from {{ ref("stg_county") }} c        
        INNER JOIN {{ ref("stg_state") }} s on c.StateName=s.StateName
    )
    

select 
*
from county