# Example 10: Python program to check if a given number is an Armstrong number

# n = 123 

number = int(input('Enter a number : '))
sum = 0
# print(len(str(number)))

for i in range():
    last_digit = number % 10
    sum += last_digit**2
    number //= 10
if sum == number:
    print('is Armstrong Number')
else:
    print('is Not Armstrong Number')