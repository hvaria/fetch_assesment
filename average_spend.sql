SELECT 
    CASE 
        WHEN AVG(CASE WHEN status = 'Accepted' THEN total_spent END) >
             AVG(CASE WHEN status = 'Rejected' THEN total_spent END) THEN 'Accepted'
        WHEN AVG(CASE WHEN status = 'Accepted' THEN total_spent END) <
             AVG(CASE WHEN status = 'Rejected' THEN total_spent END) THEN 'Rejected'
        ELSE 'Equal'
    END AS greater_average_spend
FROM fact_receipts;
