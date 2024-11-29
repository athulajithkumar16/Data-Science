import pandas as pd

df = pd.read_csv('C:/Users/lilguy/Downloads/missing_data.csv')

# print(df.isnull().sum())

# df.fillna(300, inplace=True)
# print(df)

# print(df.isnull().sum())

# -------------------------------------------------------------

# Filling the missing value in specific column

# Calories
# df['Calories'].fillna(300, inplace=True)

# df['Date'].fillna('2024/11/09', inplace=True)
# print(df)

# -------------------------------------------------------------

# 1. Mean()
# 2. Median()
# 3. Mode()

# # Mean
# df['Calories'].fillna(df['Calories'].mean(), inplace=True)

# Median
# df['Calories'].fillna(df['Calories'].median(), inplace=True)

# Mode
# df['Calories'].fillna(df['Calories'].mode()[0], inplace=True)

# df['Date'].fillna(df['Date'].mode()[0], inplace=True)

# print(df)
# -------------------------------------------------------------

# Dropna()
# df.dropna(inplace=True, ignore_index=True)     # missing value row is removed

df.dropna(subset='Calories', inplace=True)     # missing value row is removed

print(df)