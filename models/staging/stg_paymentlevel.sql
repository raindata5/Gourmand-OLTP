{% set levels = [["$", "Very Low"],["$$", "Low"],["$$$", "High"],["$$$$", "Very High"]] %}


with payments as (
    select 
    price
    from {{source("dbo", "Business")}}
    GROUP BY price
),

payments_cat as (
    select 
    ROW_NUMBER() OVER(order by price) ChainID,
    price as Price,
    CASE

    {%- for level in levels %}
    when price = '{{ level[0] }}' then '{{ level[1] }}'
    {% endfor -%}
    ELSE 'Unknown'
    END as payment_name
    from payments
) 

select * from payments_cat