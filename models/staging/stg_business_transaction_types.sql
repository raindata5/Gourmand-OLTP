-- consider placing in unknown member here to include all business even 
-- if no reported transactiontype
WITH business_tran as (
  SELECT
    tt.transactionid,
    tt.transactionname,
    t.businessalias


  FROM {{ source("dbo", "Transactions")}} t
  INNER JOIN {{ref("stg_transactiontype")}} tt on t.[transaction] = tt.transactionname
),

businessid_tran as (
  SELECT
    b.businessid,
    t.transactionid,
    t.transactionname,
    t.businessalias
  from business_tran t
  INNER JOIN {{ ref("stg_business") }} b on t.businessalias = b.BusinessName
)

select 
  businessid BusinessID,
  transactionid TransactionID
FROM businessid_tran
-- ORDER BY BusinessID, TransactionID tbd...