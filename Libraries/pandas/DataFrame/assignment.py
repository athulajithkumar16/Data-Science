import pandas as pd

df = pd.read_csv('C:/Users/lilguy/Downloads/customer1.txt', header=None)
df.columns = ['id', 'fname', 'lname', 'age', 'prof', 'location']

df = df.fillna('NaN')

# 1. Find Row count 
print(df.shape[0])
 
# 2. Remove duplicates rows and find total row count 
df = df.drop_duplicates()
print(df.shape[0])

# 3. Age maximum 10 fname,lname,prof,loc 
print(df.sort_values(by='age', ascending=False)[['fname', 'lname', 'prof', 'location']].head(10))
 
# 4. Age minimum 5 employees fname,lname,prof,loc 
print(df.sort_values(by='age')[['fname', 'lname', 'prof', 'loc']].head(5))

# 5. Each location count  [count desc order] 
print(df['location'].value_counts(ascending=False))

# 6. Full data 
print(df)
 
# 7. Each age group count [age desc order] 
print(df['age'].value_counts().sort_index(ascending=False))
 
# 8. Each profession count [count desc order] 
print(df['prof'].value_counts(ascending=False))
 
# 9. India work 
df1 = df.loc[df['location'] == 'india']
 
#           A. Row count 
print(df1.shape[0])
 
#           B. Each profession count [count desc order] 
print(df1['prof'].value_counts(ascending=False))
 
#           C. Age mxm 3 employees fname,lname,age,prof 
print(df1.sort_values(by='age', ascending=False) [['fname', 'lname', 'age', 'prof']].head(3))
 
#           D. Age minimum 3 employees fname,lname,age,prof 
print(df1.sort_values(by='age') [['fname', 'lname', 'age', 'prof']].head(3))
 
#           E. age above 40 full data 
print(df1.loc[df1['age'] > 40])
 
#           F. age range 30 to 40 [profession count] 
print(df1.loc[(df1['age'] >= 30) & (df['age'] <= 40), 'prof'].value_counts())

 
# 10. us work 
df2 = df.loc[df['location'] == 'us']

#          A. Row count 
print(df2.shape[0])
 
#          B. Each age group count 
print(df2['age'].value_counts())
 
#          C. Each profession count  [count desc] 
print(df2['prof'].value_counts(ascending=False))

 
#          D. Civil engineer dept and age above 30  
print(df2.loc[(df['prof']=='Civil engineer') & (df['age'] > 30)])