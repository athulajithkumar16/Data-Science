# 3)A number is called perfect if the sum of proper divisors of that number
# is equal to the number. For example 28 is perfect number, since 1+2+4+7+14=28.
# Write a program to print all the perfect numbers in a given range

def check_perfect(lower,upper):
    for i in range(lower, upper+1):
        sum = 0
        for j in range(1,i//2 + 1):
            if i%j == 0:
                sum += j

        if sum == i:
            print(i, end=' ')

lower = int(input('Enter lower bound : '))
upper = int(input('Enter upper bound : '))
print(check_perfect(lower,upper))