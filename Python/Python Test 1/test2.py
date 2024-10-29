number = int(input('Enter a positive integer : '))
sum = 0

while number > 0:              # 123
    last_digit = number % 10    # 3
    sum += last_digit           # 3
    number //= 10               # 12
    # print(number)

# print(sum)

print('Sum is Even' if sum%2==0 else 'Sum is Odd')