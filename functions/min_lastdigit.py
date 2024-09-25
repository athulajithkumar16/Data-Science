def minimum(num1, num2, num3):
    # return min(num1,num2,num3)
    return num1 if num2%10 > num1%10 < num3%10 else num2 if num1%10 > num2%10 < num3%10 else num3

number1 = int(input('Enter first number : '))
number2 = int(input('Enter second number : '))
number3 = int(input('Enter third number : '))

print(minimum(number1, number2, number3)) 