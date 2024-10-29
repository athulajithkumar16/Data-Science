def max_lastdigit(num1, num2):
    return num1 if num1%10 > num2%10 else num2

num1 = int(input('Enter first number : '))
num2 = int(input('Enter second number : '))

while num1 < 10 or num2 < 10:
    if num1 < 10:
        num1=int(input('Please enter a first number greater than 10 : '))
    else:
        num2=int(input('Please enter a second number greater than 10 : '))

print(max_lastdigit(num1,num2))