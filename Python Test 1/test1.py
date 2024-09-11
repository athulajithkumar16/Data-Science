num1 = int(input('Enter first number :'))
num2 = int(input('Enter second number :'))
num3 = int(input('Enter third number :'))
sum = num1 + num2 + num3

if sum > 100:
    print(f'Product of {num1}*{num2}*{num3} is {num1*num2*num3}')
elif 50 <= sum <= 100:
    print(f'Average is {round(sum/3,2)}')
elif sum < 50:
    if num1 % 5 == 0 or num2 % 5 == 0 or num3 % 5 == 0:
        print(f'Smallest number is {min(num1,num2,num3)}')
    elif num1 != 0 and num2 != 0 and num3 != 0:
        print(f'Largest number is {max(num1,num2,num3)}')