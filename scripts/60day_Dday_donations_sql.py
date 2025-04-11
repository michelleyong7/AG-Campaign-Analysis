import sqlite3
import pandas as pd

def run_query(sql, output_csv):
    conn = sqlite3.connect('data/nick_brown_campaign.db')
    df = pd.read_sql_query(sql, conn)
    df.to_csv(output_csv, index=False)
    conn.close()
    print(f"✅ Query saved to {output_csv}")

# query:donations in the last 60 days before election (Nov 5, 2024)
run_query("""
SELECT receipt_date, 
       amount, 
       contributor_city, 
       contributor_occupation
FROM contributions
WHERE receipt_date >= '2024-09-05'
ORDER BY receipt_date ASC;
""", "data/donations_last_60_days.csv")
