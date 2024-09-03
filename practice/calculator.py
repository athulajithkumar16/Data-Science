


num1 = int(input())
num2 = int(input())

operand = input('Operator (+ - * / //) : ')

# def sum(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# def floordiv(a,b):
#     return a//b

if operand == '+':
    print(f'{num1} + {num2} is {num1+num2}')
elif operand == '-':
    print(f'{num1} - {num2} is {num1-num2}')
elif operand == '*':
    print(f'{num1} * {num2} is {num1*num2}')
elif operand == '/':
    print(f'{num1} / {num2} is {num1/num2}')
elif operand == '//':
    print(f'{num1} / {num2} is {num1//num2}')
