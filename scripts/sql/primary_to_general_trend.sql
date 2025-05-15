Weekly trend between primary and general election
SELECT strftime('%Y-%W', receipt_date) AS week,
       COUNT(*) AS num_donations,
       SUM(amount) AS weekly_total,
       SUM(SUM(amount)) OVER (ORDER BY strftime('%Y-%W', receipt_date)) AS cumulative_total
FROM contributions
WHERE receipt_date BETWEEN '2024-08-06' AND '2024-11-05'
GROUP BY week
ORDER BY week;