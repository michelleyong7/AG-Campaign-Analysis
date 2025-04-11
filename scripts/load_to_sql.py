import pandas as pd
import sqlite3

# loaded clean csv from root/data
df = pd.read_csv('data/nick_brown_cleaned.csv')

# connecting sqlite to db file
conn = sqlite3.connect('data/nick_brown_campaign.db')

# saving dataframe to a table
df.to_sql('contributions', conn, if_exists='replace', index=False)

print("✅ SQLite database created and data loaded successfully.")
