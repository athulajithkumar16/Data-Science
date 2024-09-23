# 2) Write a function that finds the sum of proper divisors of a number.
# Proper divisors of a number are those numbers by which the number is divisible,
# except the number itself. For example proper divisors of 36 
# are 1, 2, 3, 4, 6, 9, 18

def sum(num):
    sum = 0
    for i in range(1,num//2 + 1):
        if num % i == 0:
            # print(i, end=' ')
            sum += i
    return sum

print(sum(12))
