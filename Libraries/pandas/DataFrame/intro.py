import pandas as pd

# nested list : id, fname, lname, age, profession, salary

employees = [[101, 'Sabu', 'Madakkassery', 24, 'Python Trainer', 25000],
            [105, 'Thejas', 'Jose', 23, 'Software Developer', 50000],
            [103, 'Sourav', 'Mohan', 27, 'Big Data', 80000],
            [104, 'Amal', 'Joby', 33, 'Unemployed', 0],
            [109, 'Aswin', 'Raj', 31, 'Sales Representative', 15000],
            [107, 'Aravind', 'V Raj', 29, 'Video Editor', 35000],
            [108, 'Amal', 'Paul', 28, 'DevOps', 90000]]

df = pd.DataFrame(employees)
df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'salary']
# print(df)

# df1 = df[['fname', 'lname', 'age', 'prof']]
# print(df1)

# FIRST 2 EMPLOYEES FNAME, LNAME, PROF, SALARY
# df1 = df[['fname', 'lname', 'prof', 'salary']].head(2)
# print(df1)

# describe
# print(df.describe())
# print(df.describe(include='O'))
# print(df.describe(include='all'))

# HOW TO ADD NEW COLUMN INTO A DATA FRAME
# df['Gender'] = ['M','F', 'M', 'M', 'F', 'F','M']
# print(df)

# df.to_csv('hello.csv')

# sort()
# sort_values()
# df1 = df.sort_values(by='age')

# df1 = df.sort_values(by='age', ascending=False)

# df1 = df.sort_values(by='fname')
# print(df1)

# ---------------------------------------------
# filter ===> loc
# loc syntax
# new_df = old_df.loc[old_df['colname'] condition ]

# # age above 28
# df1 = df.loc[df['age'] > 28]
# print(df1)

# python prof data
# df1 = df.loc[df['prof']=='Python Trainer']
# print(df1)

# big data fname, lname, age
df1 = df.loc[df['prof']=='Big Data'] [['fname', 'lname', 'age']]
print(df1)