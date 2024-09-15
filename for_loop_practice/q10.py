# Example 10: Python program to check if a given number is an Armstrong number

# n = 123 

number = int(input('Enter a number : '))
sum = 0
length = len(str(number))

for i in range(len(str(number))):
    last_digit = number % 10
    sum += last_digit**length
    number //= 10


if sum == number:
    print('is Armstrong Number')
else:
    print('is Not Armstrong Number')