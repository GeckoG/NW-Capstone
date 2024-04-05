import pandas as pd

df = pd.read_csv('Cleaned-Data.csv')

# Remove all values for year 2020
df = df[df['Year'] != 2020]

# Group by the columns and calculate the mean
grouped_df = df.groupby(['Event', 'Division', 'Sex', 'Year'])['Points'].mean().reset_index()

# Round the average points to the nearest whole number
grouped_df['Points'] = grouped_df['Points'].round(0).astype(int)

# Save the result to a new CSV file
grouped_df.to_csv('top100avg.csv', index=False)