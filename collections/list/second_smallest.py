# #SECOND SMALLEST
numbers = [1,3,8,8,4,7,2,9,11,13]

smallest = second_smallest = float('inf')
for i in numbers:
    if i < smallest:
        smallest, second_smallest = i, smallest
    elif smallest < i < second_smallest:
         second_smallest = i
print(second_smallest)