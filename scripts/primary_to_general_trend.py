import sqlite3
import pandas as pd

def run_query(sql, output_csv):
    conn = sqlite3.connect('data/nick_brown_campaign.db')
    df = pd.read_sql_query(sql, conn)
    df.to_csv(output_csv, index=False)
    conn.close()
    print(f"✅ Primary-to-General trend saved to {output_csv}")

# SQL: Weekly trend between primary and general election
run_query("""
SELECT strftime('%Y-%W', receipt_date) AS week,
       COUNT(*) AS num_donations,
       SUM(amount) AS weekly_total,
       SUM(SUM(amount)) OVER (ORDER BY strftime('%Y-%W', receipt_date)) AS cumulative_total
FROM contributions
WHERE receipt_date BETWEEN '2024-08-06' AND '2024-11-05'
GROUP BY week
ORDER BY week;
""", "data/primary_to_general_trend.csv")
