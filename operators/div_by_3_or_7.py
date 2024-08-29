num = int(input('Enter a number : '))

if num % 3 == 0 and num % 7 == 0 :
    print('Divisible by both 3 and 7')

elif num % 3 == 0 or num % 7 == 0 :
    print('Divisible by either 3 or 7')