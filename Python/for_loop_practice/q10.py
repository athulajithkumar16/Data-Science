# Example 10: Python program to check if a given number is an Armstrong number

number = int(input('Enter a number : '))
dummy_number = number
sum = 0
length = len(str(number))

for i in range(len(str(number))):
    last_digit = number % 10
    sum += last_digit**length
    number //= 10

if sum == dummy_number:
    print('is Armstrong Number')
else:
    print('is Not Armstrong Number')