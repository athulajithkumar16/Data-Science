number = int(input('Enter a number : '))
dummy_number = number
sum = 0

while number > 0:
    last_digit = number % 10
    sum += last_digit**len(str(dummy_number))
    number //=10

if sum == dummy_number:
    print('is Armstrong Number')
else:
    print('is Not Armstrong Number')