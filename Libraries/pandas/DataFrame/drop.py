import pandas as pd

employees = [[101, 'Sabu', 'Madakkassery', 24, 'Python Trainer', 25000],
            [105, 'Thejas', 'Jose', 23, 'Software Developer', 50000],
            [103, 'Sourav', 'Mohan', 27, 'Big Data', 80000],
            [104, 'Amal', 'Joby', 33, 'Unemployed', 0],
            [109, 'Aswin', 'Raj', 31, 'Sales Representative', 15000],
            [107, 'Aravind', 'V Raj', 29, 'Video Editor', 35000],
            [108, 'Amal', 'Paul', 28, 'DevOps', 90000],
            [104, 'Amal', 'Joby', 33, 'Unemployed', 0]
            ]

df = pd.DataFrame(employees)
df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'salary']
# df1 = df.drop(['fname', 'id'], axis=1)

# drop_duplicates
df1 = df.drop_duplicates()
print(df1)