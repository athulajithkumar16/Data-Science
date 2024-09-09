num1 = int(input('Enter a number : '))
num2 = int(input('Enter another number : '))

# METHOD 1
#  i = 1
# while i <= min(num1,num2):
#     if num1 % i == 0 and num2 % i == 0:
#         # print(i, end=' ')
#         hcf= i
#     i += 1

# print(f'HCF of {num1} and {num2} is {hcf}')

# METHOD 2

i = min(num1, num2)

while i <= min(num1,num2):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i
        break
    i -=1
print(hcf)

# METHOD 3
while 