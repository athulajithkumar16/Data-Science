import pandas as pd

df = pd.read_csv('C:/Users/lilguy/Downloads/txn.csv')
# print(df)

# 1. Find Row count 
print(df.shape[0])

# 2. jan month oid,cusno,category,product,state 
df_jan = df.loc[df['dat'].str[:2] == '01'] [['oid', 'cid', 'category', 'product', 'state']]
# print(df_jan)

# A. Row count 
print(df_jan.shape[0])

# 3. July Month oid,cusno,category,product,state 
df_july = df.loc[df['dat'].str[:2] == '07'] [['oid', 'cid', 'category', 'product', 'state']]

# B. Row count 
print(df_july.shape[0])


# 4. Each category [count desc sort] 
df1 = df.groupby('category') ['category'].count() \
    .sort_values(ascending=False)

# 5. Category full details 
df2 = df.loc[df['category'] == df1.idxmax()]

# 6. Each paymethod count 
df3 = df.groupby(by='method')['method'].count()

# 7. jan-july month purchase count [include] 
df4 = df.loc[df['dat'].str[:2].isin(['01', '02', '03', '04', '05', '06', '07'])].sort_values(by='dat') [['oid', 'cid','dat', 'category', 'product', 'state']]

# 8. Each category total amount 
df4 = df.groupby(by='category') ['amount'].sum()

# 9. Each category maximum amount 
df5 = df.groupby(by='category') ['amount'].max()

# 10. Each category avg amount 
df6 = df.groupby(by='category') ['amount'].mean()

# 11.total amount by cash and credit card 
df7 = df.groupby(by='method') ['amount'].sum()

# 12. Indoor games ,total amount 
df8 = df.groupby(by='category') ['amount'].sum() .loc['Indoor Games']

# 13. Each state count 
df9 = df.groupby(by='state') ['state'].count() \
                .sort_values()