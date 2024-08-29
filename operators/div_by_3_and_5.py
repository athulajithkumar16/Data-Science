num = int(input('Enter a number : '))

if num%3 == 0 and num%5 == 0:
    print(f'{num} divisible by both 3 and 5')
elif num%3 == 0:
    print(f'{num} divisible by 3 only')
elif num%5 == 0:
    print(f'{num} divisible by 5 only')

else:
    print(False)