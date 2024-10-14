# 5 Write a Python program that takes a list of numbers as input from the user and 
# prints out the maximum and minimum numbers in the list.

numbers = list(map(int, input('Enter numbers seperated by spaces : ').split()))

largest = float('-inf')
smallest = float('inf')

for i in numbers:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i

print(f'Largest Number - {largest} \nSmallest Number - {smallest}')