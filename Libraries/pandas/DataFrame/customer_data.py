import pandas as pd

# df = pd.read_csv('hello.csv', sep=',')
# print(df)

# header tag
# if the file doesnt contain HEADER TAG
# mention
# header = None
# df = pd.read_csv('hello.csv', sep=',', header=None)


df = pd.read_csv('C:/Users/lilguy/Downloads/customer1.txt', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'location']

# print(df)

# print(df.columns)

# Total number of missing values
# print(df.isna().sum())

# How to fill missing value
# df = df.fillna('India')

# # 1. first 25 emp fname, lname, age
# df1 = df[['fname', 'lname', 'age']].head(25)
# print(df1)

# # 2. last 10 emp fname, lname, prof
# df2 = df[['fname', 'lname', 'age', 'prof']].tail(10)
# print(df2)
# -----------------------------------------

# INDEX ILOC
# 25th row
# 10-30 rows
# iloc
# df1 = df.iloc[24]   #25th ROW
# print(df1)

# # 10-20 rows
# df1 = df.iloc[10:21]
# print(df1)

# df1 = df.iloc[10:21:2]
# print(df1)

# # COLUMN 
# df1 = df.iloc[3:31, 1:5]
# print(df1)

# df1 = df.iloc[1::5, :4]
# print(df1)

# x = last column
# y = last_column
x = df.iloc[:,:-1]
y = df.iloc[:, -1]
print(x)
print(y)


# -----------------------------------------------------------------
# df1 = df.loc[(df['prof']=='python') & (df['age']>21)] [['fname', 'lname', 'age']]
# print(df1)