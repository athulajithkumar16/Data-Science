# Inner Joining

# nested_dic ==> id, fname, lname, age
# dict2 ===> prof, salary, id, location

import pandas as pd

dict1 = {'id' : [1,2,3,4,5], 'fname': ['vimal', 'amal', 'surya', 'athul', 'issak'],
         'lname':['joy', 'paul', 'sudheer', 'ajith', 'thomas'],
         'age' : [23, 19, 25, 29, 31]}

dict2 = {'prof': ['bigdata', 'python', 'testing', 'hr', 'ceo'],
         'salary': [2000, 1700, 1300, 2500, 4000],
         'id': [4,5,6,7,8], 
         'location': ['Kakkanad', 'Edappilly', 'Kalamassery', 'Kadavanthara', 'Kumbalangi']}

df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)

print(df1)
print(df2)

# inner joining
# df3 = pd.merge(df1, df2, on='id', how='inner') [['fname', 'lname', 'age', 'prof', 'salary']]

df3 = pd.merge(df1, df2, on='id', how='inner') \
     .loc[df1['age'] > 27] [['fname', 'lname', 'age', 'prof']]

print(df3)