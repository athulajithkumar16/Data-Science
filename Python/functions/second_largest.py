# WRITE A FUNCTION TO IDENTIFY SECOND SMALLEST AMONG 3 NUMBERS

# def second_min(num1,num2,num3):
#     minimum = min(num1,num2,num3)
#     maximum = max(num1,num2,num3)
#     if minimum < num1 < maximum:
#         return num1
#     elif minimum < num2 < maximum:
#         return num2
#     elif minimum < num3 < maximum:
#         return num3
    
number1 = int(input('Enter first number : '))
number2 = int(input('Enter second number : '))
number3 = int(input('Enter third number : '))
minimum = min(number1, number2, number3)
maximum = max(number1, number2, number3)

second_min = lambda num1, num2, num3 : num1 if minimum<num1<maximum else num2 if minimum<num2<maximum else num3
    
second_max = lambda num1, num2, num3 : num1 if minimum<num1<maximum else num2 if minimum<num2<maximum else num3

print(second_min(number1, number2, number3))