# METHOD 1
# def reverse(string):
#     print(string[::-1])

# test = input('Enter the number : ')
# reverse(test)


# METHOD 2
def reverse(num):
    rev = 0
    while num > 0:
        last_digit = num % 10
        rev = rev * 10 + last_digit
        num //= 10
    print(rev)
reverse(134)