import sqlite3
import pandas as pd

def run_query(sql, output_csv):
    conn = sqlite3.connect('data/nick_brown_campaign.db')
    df = pd.read_sql_query(sql, conn)
    df.to_csv(output_csv, index=False)
    conn.close()
    print(f"✅ Query saved to {output_csv}")

#run top cities query
run_query("""
SELECT contributor_city,
       COUNT(*) AS donation_count,
       SUM(amount) AS total_donated
FROM contributions
GROUP BY contributor_city
ORDER BY total_donated DESC
LIMIT 10;
""", "data/top_donor_cities.csv")
