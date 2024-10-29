def is_leapyear(year):
    if year % 4 == 0 and year % 100!= 0:
        return 'LEAP YEAR'
    elif year % 100 == 0 and year % 400!= 0:
        return 'NOT LEAP YEAR'
    elif year % 400 == 0:
        return 'LEAP YEAR'
    else:
        return 'NOT LEAP YEAR'
    
year = int(input('Year : '))
print(is_leapyear(year))