age = int(input('Enter age : '))
sex = input('Enter sex ( M/F) : ')
number_of_days = int(input('Number of days you worked : '))


if age >= 18 and age < 30:
    if sex.lower() == 'm':
        print(f'Total Wages : {number_of_days*700}')
    elif sex.lower() == 'f':
        print(f'Total Wages : {number_of_days*750}')
elif age >= 30 and age <= 40:
    if sex.lower() == 'm':
        print(f'Total Wages : {number_of_days*800}')
    elif sex.lower() == 'f':
        print(f'Total Wages : {number_of_days*850}')