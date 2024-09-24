# FUNCTION TO CHECK WHETHER A GIVEN NUMBER IS PRIME OR NOT
def prime_or_not(num):
    flag = 0
    for i in range(2,num//2 + 1):
        if num % i == 0:
            flag = 1

    if flag == 0:
        print('PRIME')
    else:
        print('NOT PRIME')

prime_or_not(num=int(input('Enter a number to check prime or not : ')))

# FUNCTION TO PRINT PRIME NUMBERS BETWEEN A GIVEN LOWER BOUND AND UPPER BOUND
def prime(lower,upper):
    flag = 0
    for i in range(lower, upper+1):
        flag = 0
        for j in range(2,i//2 + 1):
            if i%j == 0:
                # print(j,end=' ')
                flag = 1
        if flag == 0:
            print(i, end=' ')

prime(lower=int(input('Lower bound : ')), upper=int(input('Upper bound : ')))
                


