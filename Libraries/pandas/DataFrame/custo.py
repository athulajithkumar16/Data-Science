import pandas as pd

df = pd.read_csv('C:/Users/lilguy/Downloads/customer1.txt', header=None)
df.columns = ['id','fname', 'lname', 'age', 'prof', 'loc']

# print(df.isna().sum())

df1 = df.fillna('india')

x = df.iloc[:, :-1]
y = df.iloc[:, -1]

df2 = df[['fname', 'lname', 'age', 'prof']]

df_ = df.loc[df['age'] > 50] [['fname', 'lname', 'age', 'prof']]

df4 = df.loc[(df['age'] >= 25 )& (df['age'] <= 40)] [['fname', 'lname', 'prof']]

df5 = df.sort_values(by='age', ascending=False) [['fname', 'lname', 'age', 'prof']].head(5)

# 8
df6 = df.sort_values(by='age') [['fname', 'lname', 'age', 'prof', 'loc']].head(3)

df7 = df.loc[df['loc'] == 'india'] [['fname', 'lname', 'age','prof', 'loc']]

df8 = df.loc[(df['loc'] == 'india') & (df['prof']=='doctor')] [['fname', 'lname','age']]

df9 = df.loc[df['loc'] == 'us'].sort_values(by='age') [['fname', 'lname', 'age']].head(3)

df10 = df.loc[(df['prof']=='actor') & (df['age'] > 50)] [['fname', 'lname', 'age']]

df11 = df.loc[df['prof'] == 'pilot'].sort_values(by='age') [['fname', 'lname', 'age', 'loc']].head(2)

df12 = df.loc[df['prof'] == 'pilot'].sort_values(by='age', ascending=False) [['fname', 'lname', 'age']].head(1)

df13 = df.loc[(df['loc'] == 'india') & (df['age'] >= 25) & (df['age'] <= 40)] [['fname', 'lname', 'age']]
print(df13)