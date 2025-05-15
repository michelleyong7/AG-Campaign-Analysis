# query: cumulative donations over time
SELECT receipt_date,
       SUM(amount) OVER (ORDER BY receipt_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_total
FROM contributions
ORDER BY receipt_date;
