# # SECOND LARGEST
numbers = [1,3,8,8,4,7,2,9,11,13]

largest = second_largest = float('-inf')
for i in numbers:
    if i > largest:
        largest, second_largest = i, largest
print(second_largest)