def minimum(num1, num2, num3):
    # return min(num1,num2,num3)
    return num1 if num2%10 > num1%10 < num3%10 else num2 if num1%10 > num2%10 < num3%10 else num3

number1 = int(input('Enter first number : '))
number2 = int(input('Enter second number : '))
number3 = int(input('Enter third number : '))

while number1 < 10 or number2 < 10 or number3 < 10:
    if number1 < 10:
        number1=int(input('Please enter a first number greater than 10 : '))
    elif number1 < 10:
        number2=int(input('Please enter a second number greater than 10 : '))
    elif number3 < 10:
        number3=int(input('Please enter a third number greater than 10 : '))


print(minimum(number1, number2, number3)) 