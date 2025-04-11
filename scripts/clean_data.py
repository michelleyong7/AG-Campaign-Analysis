import pandas as pd

# Load the CSV
df = pd.read_csv('data/nick_brown_contributions.csv')

# Convert date to datetime format
df['receipt_date'] = pd.to_datetime(df['receipt_date'])

# Extract month and year
df['month'] = df['receipt_date'].dt.to_period('M')
df['year'] = df['receipt_date'].dt.year

# Clean up occupation and employer columns
df['contributor_occupation'] = df['contributor_occupation'].str.strip().str.lower().fillna('unknown')
df['contributor_employer_name'] = df['contributor_employer_name'].str.strip().str.lower().fillna('unknown')

# Clean city/state/zip
df['contributor_city'] = df['contributor_city'].str.title()
df['contributor_state'] = df['contributor_state'].fillna('WA')
df['contributor_zip'] = df['contributor_zip'].astype(str).str[:5]

# Drop unnecessary columns for this analysis
columns_to_drop = ['url', 'committee_id', 'filer_id', 'origin', 'code']
df_cleaned = df.drop(columns=columns_to_drop)

# Optional: Filter to just cash contributions
df_cash = df_cleaned[df_cleaned['cash_or_in_kind'].str.lower() == 'cash']

# Save cleaned file
df_cleaned.to_csv('data/nick_brown_cleaned.csv', index=False)

