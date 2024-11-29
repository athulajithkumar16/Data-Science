import pandas as pd

# id, fname, lname, sub1, sub2, sub3, college_name

students = [[105, 'Amal', 'Paul', 67, 98, 56, 'Christ College'],
            [120, 'Thejas', 'SUbramanian', 84, 56, 24, 'IIT Delhi'],
            [117, 'Amal', 'Joby', 34, 20, 0, 'IIT Nadavaramb'],
            [160, 'Suryanath', 'Gopi', 70, 86, 95, 'Vidya Engineering College'],
            [142, 'Rizwan', 'Shafeek', 77, 54, 10, 'NMIT Bangalore']]

df = pd.DataFrame(students)

df.columns = ['id', 'Fname','lname', 'sub1', 'sub2', 'sub3', 'college name']

# print(df)

# print(df.shape)
# print(df.dtypes)

print(df.head(3))   # first three rows

print(df.tail(2))   # last two rows