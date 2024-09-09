# METHOD 1
# num = int(input('Enter the number : '))
# i,fact = 1, 1

# while i <= num :
#     fact *= i
#     i += 1

# print(fact)

# METHOD 2 - Decrementing
num = int(input('Enter the number : '))
temp = num
fact = 1

while num > 0:  # or num >= 1
    fact *= num
    num -= 1

print(f'Factorial of {temp} is {fact}')

