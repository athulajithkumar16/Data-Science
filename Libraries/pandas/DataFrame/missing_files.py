# Data Frame

# column names
# find total number of missing values
# 250 value missing fill

import pandas as pd

df = pd.read_csv('C:/Users/lilguy/Downloads/missing_data.csv')

print(df.columns)

print(df.isna().sum())

df1 = df.fillna(250)
print(df1)
print(df1.isna().sum())
