import pandas as pd

# Load the CSV file
df = pd.read_csv('train.csv')

# Remove rows where any of the specified columns are empty or NaN
df_cleaned = df.dropna(subset=['category', 'sub_category', 'crimeaditionalinfo'])

# Optionally, filter out rows where these columns are empty strings
df_cleaned = df_cleaned[(df_cleaned['category'] != '') &  
                        (df_cleaned['sub_category'] != '') &  
                        (df_cleaned['crimeaditionalinfo'] != '')]

# Drop rows where the 'sub_category' is 'others' or 'other'
df_cleaned = df_cleaned[~df_cleaned['sub_category'].str.lower().isin(['others', 'other'])]

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('cleaned_train.csv', index=False)

# Print the first few rows of the cleaned DataFrame to verify
print(df_cleaned.head())
