-- {{ generate_schema_name("Production", {"name": "PaymentLevel", "resource_type": "model"}) }}

with paymentlevels as (
    SELECT *
    from {{ref("stg_paymentlevel")}}
)

SELECT *
FROM paymentlevels