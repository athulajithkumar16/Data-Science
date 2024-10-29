# Example 4: Python program to calculate the sum of all the odd numbers within the given range.

given_range = int(input('Enter range : '))
sum = 0

for i in range(given_range+1):
    if i%2 != 0:
        sum += i

print(sum)
