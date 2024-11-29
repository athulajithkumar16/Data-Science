import pandas as pd

nested_dict = {'id': [1,2,3,4,5],
                'fname': ['amal', 'sabu', 'niya', 'vivek', 'surya'],
                'lname' : ['joby', 'paul', 'ross', 'babu', 'george'],
                'age': [27, 29, 23, 30, 33],
                'prof': ['bigdata', 'python', 'testing', 'development', 'devops'],
                'salary': [15000, 24000, 20000, 35000, 80000]}

df = pd.DataFrame(nested_dict)
# print(df)

print(df.shape)