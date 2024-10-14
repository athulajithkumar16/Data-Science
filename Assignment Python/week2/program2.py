# 2  Write a program to check whether given year is leap year or not

year = int(input('Year : '))

if year % 4 == 0 and year % 100!= 0:
    print('Leap year')
elif year % 100 == 0 and year % 400!= 0:
    print('Not Leap Year')
elif year % 400 == 0:
    print('Leap Year')
else:
    print('Not Leap Year')