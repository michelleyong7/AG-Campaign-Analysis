import sqlite3
import pandas as pd

def run_query(sql, output_csv):
    conn = sqlite3.connect('data/nick_brown_campaign.db')
    df = pd.read_sql_query(sql, conn)
    df.to_csv(output_csv, index=False)
    conn.close()
    print(f"✅ Query saved to {output_csv}")

# query: cumulative donations over time
run_query("""
SELECT receipt_date,
       SUM(amount) OVER (ORDER BY receipt_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_total
FROM contributions
ORDER BY receipt_date;
""", "data/cumulative_donations.csv")
