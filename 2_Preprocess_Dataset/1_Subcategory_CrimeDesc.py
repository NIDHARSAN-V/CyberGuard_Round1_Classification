import pandas as pd

# Load the CSV file
df = pd.read_csv('cleaned_train.csv')

# Remove rows where 'sub_category' or 'crimeaditionalinfo' are empty or NaN
df_cleaned = df.dropna(subset=['sub_category', 'crimeaditionalinfo'])

# Optionally, filter out rows where these columns are empty strings
df_cleaned = df_cleaned[(df_cleaned['sub_category'] != '') &   
                        (df_cleaned['crimeaditionalinfo'] != '')]

# Drop the 'category' column
df_cleaned = df_cleaned.drop(columns=['category'])

# Save the cleaned DataFrame to a new CSV file
df_cleaned.to_csv('sub_desc.csv', index=False)

# Print the first few rows of the cleaned DataFrame to verify 
print(df_cleaned.head())
