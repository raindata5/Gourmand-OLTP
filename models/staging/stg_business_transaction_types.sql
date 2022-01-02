-- consider placing in unknown member here to include all business even 
-- if no reported transactiontype
WITH business_tran as (
  SELECT
    distinct
    tt.TransactionID,
    tt.TransactionName,
    t.businessalias


  FROM {{ source("public", "Transactions")}} t
  INNER JOIN {{ref("stg_transactiontype")}} tt on t."transaction" = tt."TransactionName"
),

businessid_tran as (
  SELECT
    b.businessid,
    t.TransactionID,
    t.TransactionName,
    t."businessalias"
  from business_tran t
  INNER JOIN {{ ref("stg_business") }} b on t.businessalias = b.BusinessName
)

select 
  businessid BusinessID,
  TransactionID TransactionID,
  cast(now() as timestamp(3) without time zone) LastEditedWhen
FROM businessid_tran
-- ORDER BY BusinessID, TransactionID tbd...