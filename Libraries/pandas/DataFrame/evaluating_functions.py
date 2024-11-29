import pandas as pd

# employees = [[101, 'Sabu', 'Madakkassery', 24, 'Python Trainer', 25000],
#             [105, 'Thejas', 'Jose', 23, 'Software Developer', 50000],
#             [103, 'Sourav', 'Mohan', 27, 'Big Data', 80000],
#             [104, 'Amal', 'Joby', 33, 'Unemployed', 0],
#             [109, 'Aswin', 'Raj', 31, 'Sales Representative', 15000],
#             [107, 'Aravind', 'V Raj', 29, 'Video Editor', 35000],
#             [108, 'Amal', 'Paul', 28, 'DevOps', 90000],
#             [102, 'Athul', 'K A', 28, 'DevOps', 90000]
#             ]
# df = pd.DataFrame(employees)
# df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'salary']

# EVALUATING FUNCTIONS

# count()   max()   min()   sum()   mean()

# groupby

# new_df = old_df.groupby('colname') ['colname'].cout()

# df1 = df.groupby('prof') ['prof'].count()

# df1 = df.groupby('prof') ['prof'].count() \
#         .sort_values(ascending=False)
# print(df1)


# ----------------------------------------------------
# df = pd.read_csv('C:/Users/lilguy/Downloads/customer1.txt', header=None)
# df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'location']

# df1 = df.groupby('prof') ['prof'].count().sort_values(ascending=False)
# print(df1)

# df2 = df.groupby('location') ['location'].count().sort_values(ascending=False)

# df3 = df.loc[df['location'] == 'india'] \
#         .groupby('prof') ['prof'].count() \
#         .sort_values(ascending=False)
# ----------------------------------------------------

# df = pd.read_csv('C:/Users/lilguy/Downloads/customer1.txt', header=None)
# df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'location']

# max()

# new_df = old_df.groupby('col_name1') ['col_name2'].max()

# each profession max age
# df1 = df.groupby('prof') ['age'].max()
# df1 = df.groupby('prof') ['age'].max() \
#         .sort_values(ascending=False)
# print(df1)

# # # each location max age
# df1 = df.groupby('location') ['age'].max() \
#         .sort_values(ascending=False)
# print(df1)

# ----------------------------------------------------

# df = pd.read_csv('C:/Users/lilguy/Downloads/Temperature',sep=' ', header=None)
# df.columns = ['year', 'temp']

# Max Temp of each year
# df1 = df.groupby('year') ['temp'].max() \
#         .sort_values(ascending=False)
# print(df1)

# Min Temp of each year
# df1 = df.groupby('year') ['temp'].min() \
#         .sort_values(ascending=False)
# print(df1)

# # Sum of Temp of each year
# df1 = df.groupby('year') ['temp'].sum() \
#         .sort_values(ascending=False)
# print(df1)

# Mean of Temp of each year
# df1 = df.groupby('year') ['temp'].mean() \
#         .sort_values(ascending=False)
# print(df1)

# ----------------------------------------------------

# df = pd.read_csv('C:/Users/lilguy/Downloads/customer5.txt', header=None)
# df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'location', 'salary']

# # each profession count [count desc ]
# df1 = df.groupby('prof') ['prof'].count() \
#         .sort_values(ascending=False)
# # print(df1)

# # each profession max salary [ salary desc ]
# df2 = df.groupby('prof') ['salary'].max()\
#         .sort_values(ascending=False)
# # print(df2)

# # each profession min salary [ salary asc ]
# df3 = df.groupby('prof') ['salary'].min() \
#         .sort_values()
# # print(df3)

# # each location total salary 
# df4 = df.groupby('location') ['salary'].sum()
# # print(df4)

# # each profession average age
# df5 = df.groupby('prof') ['age'].mean() \
#         .round()
# # print(df5)

# ----------------------------------------------------

