SELECT b.name AS brand_name, COUNT(fri.receipt_id) AS receipts_scanned
FROM fact_receipt_items fri
JOIN dim_brands b ON fri.brand_id = b.brand_id
JOIN fact_receipts fr ON fri.receipt_id = fr.receipt_id
JOIN dim_dates d ON fr.purchase_date_id = d.date_id
WHERE d.full_date >= DATE_TRUNC('month', CURRENT_DATE - INTERVAL '1 month')
  AND d.full_date < DATE_TRUNC('month', CURRENT_DATE)
GROUP BY b.name
ORDER BY receipts_scanned DESC
LIMIT 5;
