import pandas as pd

df1 = pd.read_csv('C:/Users/lilguy/Downloads/custom.txt', header=None)
df1.columns = ['id', 'name', 'age', 'location', 'salary']

df2 = pd.read_csv('C:/Users/lilguy/Downloads/order.txt', header=None)
df2.columns = ['order_id', 'date', 'id', 'amount']

# perform inner joining
# df3 = pd.merge(df1, df2, on='id', how='inner')

# salary above 2500 fname, age, salary, date, amount
df3 = pd.merge(df1, df2, on='id', how='inner') \
        .loc[df1['salary'] > 2500] [['name', 'age', 'salary', 'date', 'amount']]
# max age 1 emp_name, age, salary, date, amount
df3 = pd.merge(df1, df2, on='id', how='inner') \
        .sort_values(by='age', ascending=False) .head(1) [['name', 'age', 'salary', 'date', 'amount']]

# latest date purchase name, age, date, amount
df3 = pd.merge(df1, df2, on='id', how='inner') \
        .sort_values(by='date', ascending=False) .head(1) [['name', 'age', 'date', 'amount']]

print(df3)