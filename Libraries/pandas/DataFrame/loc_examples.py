import pandas as pd

df = pd.read_csv('C:/Users/lilguy/Downloads/sample4.txt', header=None)
df.columns = ['slno', 'fname', 'lname', 'age', 'phno', 'loc']

# age above 22 fname, lname, age
# df1 = df.loc[df['age'] > 22] [['fname', 'lname', 'age']]
# print(df1)

# age = 24 fname lname loc

# df2 = df.loc[df['age'] == 24][['fname', 'lname', 'loc']]

# df3 = df.loc[df['loc'] == 'Chennai']

# df4 = df.loc[(df['age'] > 23) & (df['loc']=='Chennai')] \
#     [['fname', 'lname', 'age', 'phno']]
# print(df4)

# LOC SORT COLUMNS HEAD/TAIL

# # Age mxm 2 emp fname lname, age,phno
df2 = df.sort_values(by='age', ascending=False)[['fname', 'lname', 'age', 'phno']].head(2)
print(df2)
# # # age minimum 1 employee fname, lname, age
df3 = df.sort_values(by='age') [['fname', 'lname', 'age']].head(1)
print(df3)

# # # Chennai work, age mxm 1 employee fname, lname, age
df4 = df.loc[df['loc']=='Chennai'].sort_values(by='age', ascending=False)[['fname', 'lname', 'age']].head(1)
print(df4)