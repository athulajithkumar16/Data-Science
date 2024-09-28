# Check the largest element in list 
# largest, smallest, second largest, second smallest

numbers = [1,3,8,8,4,7,2,9,11,13]

# # LARGEST ELEMENT IN LIST
largest = float('-inf')
for i in numbers:
    if i > largest:
        largest = i

# print(largest)