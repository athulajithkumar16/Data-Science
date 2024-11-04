# number = int(input('Enter the number : '))

# while number >= 0:
#     print(number)
#     number = int(input('Enter the number : '))

numbers = list(map(int, input('Enter numbers in space seperated : ').split()))

for i in numbers:
    if i < 0:
        break
    print(i)