import sqlite3
import pandas as pd
conn=sqlite3.connect('data/nick_brown_campaign.db')
#total contribution query
query=""" 
SELECT strftime('%Y-%m', receipt_date) AS month,
    SUM(amount) AS total_amount
FROM contributions
GROUP BY month 
ORDER BY month;
"""
#runquery
df=pd.read_sql_query(query,conn)
#results
print(df)
df.to_csv('data/contributions_by_month.csv', index=False)
conn.close()
