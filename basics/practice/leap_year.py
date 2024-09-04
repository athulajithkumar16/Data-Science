'''
Century Year
Non Century year
'''

year = int(input('Year : '))

if year % 4 == 0 and year % 100!= 0:
    print('Leap year')
elif year % 100 == 0 and year % 400!= 0:
    print('Not Leap Year')
elif year % 400 == 0:
    print('Leap Year')
else:
    print('Not Leap Year')