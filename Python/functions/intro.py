# input()
# print()
# range()
# len()

# def functionName():
#     statements
# functionName()

# def greet():    # function header
#     print('Welcome 2025')   #function body

# greet()     # function caller


# def details(name,rollno):
#     print(f'Name : {name} Roll No. : {rollno}')

# details(name='Aalfin', rollno=52)   # KEYWORD ARGUMENT


def info(name, rollno, course='DataScience'):       # DEFAULT PARAMETER
    print(f'Name : {name}, RollNo : {rollno}, Course : {course}')

# info('shubham',23)

# info('athul', 22, course='PythonFullStack')

size = int(input('Enter number of ppl to enter'))
for i in range(size):
    info(input('Name : '), input('Roll No :'), input('Course : '))