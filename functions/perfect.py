# PROGRAM TO CHECK WHETHER A NUMBER IS PERFECT OR NOT
# A number is called perfect if the sum of proper divisors of that number
# is equal to the number. For example 28 is perfect number, since 1+2+4+7+14=28.

def check_perfect(num):
    sum = 0
    for i in range(1,num//2 + 1):
        if num % i == 0:
            sum += i

    return 'PERFECT NUMBER' if num == sum else 'NOT PERFECT'

number = int(input('Enter a number : '))
print(check_perfect(number))