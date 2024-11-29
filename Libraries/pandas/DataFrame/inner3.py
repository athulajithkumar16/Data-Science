import pandas as pd

df1 = pd.read_csv('C:/Users/lilguy/Downloads/student.unknown', header=None)
df1.columns = ['name', 'rollno']

df2 = pd.read_csv('C:/Users/lilguy/Downloads/results.unknown', header=None)
df2.columns = ['rollno', 'result']

# pass 
df3 = pd.merge(df1, df2, on='rollno', how='inner') \
        .loc[df2['result'] == 'pass'] [['name', 'rollno', 'result']]

print(df3)