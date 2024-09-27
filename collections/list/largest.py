# Check the largest element in list 
# largest, smallest, second largest, second smallest

numbers = [1,3,8,8,4,7,2,9,11,13]

# # LARGEST ELEMENT IN LIST
# largest = float('-inf)
# for i in numbers:
#     if i > largest:
#         largest = i

# print(largest)

# # SMALLEST ELEMENT IN LIST
# smallest = float('inf')
# for i in numbers:
#     if i < smallest:
#         smallest = i
# print(smallest)

# # SECOND LARGEST
# largest = second_largest = float('-inf')
# for i in numbers:
#     if i > largest:
#         largest, second_largest = i, largest
# print(second_largest)

# #SECOND SMALLEST
smallest = second_smallest = float('inf')
for i in numbers:
    if i < smallest:
        smallest, second_smallest = i, smallest
    elif smallest < i < second_smallest:
         second_smallest = i
print(second_smallest)