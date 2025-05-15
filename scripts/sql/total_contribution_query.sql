#total contribution query
SELECT strftime('%Y-%m', receipt_date) AS month,
    SUM(amount) AS total_amount
FROM contributions
GROUP BY month 
ORDER BY month;