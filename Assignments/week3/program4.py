number = int(input('Enter a number : '))
test = number
number_of_digits = len(str(number))
sum_of_digits = 0

for i in range(number_of_digits):
    last_digit = number % 10
    sum_of_digits += last_digit**number_of_digits
    number //= 10

if sum_of_digits == test:
    print('Armstrong')
else:
    print('Ain\'t Armstrong')