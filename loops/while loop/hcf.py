num1 = int(input('Enter a number : '))
num2 = int(input('Enter another number : '))
i = 1

while i <= min(num1,num2):
    if num1 % i == 0 and num2 % i == 0:
        print(i, end=' ')
    i += 1