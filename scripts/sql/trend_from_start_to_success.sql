
--Weekly trend from launch to Nov 2024
SELECT strftime('%Y-%W', receipt_date) AS week,
       COUNT(*) AS num_donations,
       SUM(amount) AS weekly_total,
       SUM(SUM(amount)) OVER (ORDER BY strftime('%Y-%W', receipt_date)) AS cumulative_total
FROM contributions
GROUP BY week
ORDER BY week;
