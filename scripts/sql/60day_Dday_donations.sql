# query:donations in the last 60 days before election (Nov 5, 2024)
SELECT receipt_date, 
       amount, 
       contributor_city, 
       contributor_occupation
FROM contributions
WHERE receipt_date >= '2024-09-05'
ORDER BY receipt_date ASC;
