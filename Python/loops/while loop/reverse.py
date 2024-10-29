# Program to reverse a number

num = int(input('Enter a number : '))

# METHOD 1
reverse = 0
while num!=0 :
    last_digit = num % 10
    reverse = reverse * 10  + last_digit
    num //=10
print(reverse)

# METHOD 2
# reverse = ''
# while num > 0:
#     last_digit = num % 10
#     reverse += str(last_digit)
#     num = num //10
# print(reverse)

# METHOD 3
# print(str(num)[::-1])
#           [start,stop,step]

# METHOD 4
# while num > 0:
#     last_digit = num % 10
#     print(last_digit, end='')
#     num = num // 10