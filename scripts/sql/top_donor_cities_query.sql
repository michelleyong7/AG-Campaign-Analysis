#run top cities query
SELECT contributor_city,
       COUNT(*) AS donation_count,
       SUM(amount) AS total_donated
FROM contributions
GROUP BY contributor_city
ORDER BY total_donated DESC
LIMIT 10;
