# Example 7: Python program to count the total number of digits in a number.

# n = str(4938234)
# print(len(n))

n = int(input('Number : '))
count = 0

for i in str(n):
    # print(i)
    count += 1
print(count)