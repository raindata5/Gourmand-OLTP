-- {% set levels = [["$", "Very Low"],["$$", "Low"],["$$$", "High"],["$$$$", "Very High"]] %}
{% set levels = [[1, "Very Low"],[2, "Low"],[3, "High"],[4, "Very High"]] %}
{% set levels2 = [[1, "$"],[2, "$$"],[3, "$$$"],[4, "$$$$"]] %}

with payments as (
    select 
    price
    from {{source("public", "Business")}}
    GROUP BY price
),

payments_cat as (
    select 
    ROW_NUMBER() OVER(order by price) PaymentLevelID,
    CASE

    {%- for level in levels2 %}
    when length(price) = '{{ level[0] }}' then '{{ level[1] }}'
    {% endfor -%}
    ELSE 'Unknown'
    END as PaymentLevelSymbol,

    CASE

    {%- for level in levels %}
    when length(price) = '{{ level[0] }}' then '{{ level[1] }}'
    {% endfor -%}
    ELSE 'Unknown'
    END as PaymentLevelName
    from payments
) ,
groups as (
select 
	distinct
    PaymentLevelSymbol,
    PaymentLevelName
from payments_cat
) 
select 
    ROW_NUMBER() OVER( order by length(PaymentLevelSymbol) ASC) PaymentLevelID,
    PaymentLevelSymbol,
    PaymentLevelName,
    cast(now() as timestamp(3) without time zone) LastEditedWhen
from groups