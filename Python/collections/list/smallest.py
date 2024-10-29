# # SMALLEST ELEMENT IN LIST
numbers = [1,3,8,8,4,7,2,9,11,13]

smallest = float('inf')
for i in numbers:
    if i < smallest:
        smallest = i
print(smallest)