# numbers = [1, 2, 3, 4]

# MAP
# def square(num):
#     return num**2
# print(list(map(square, numbers)))

# print(list(map(lambda num : num**2, numbers)))

# numbers = [1,2,3,4,5,6,7,8]
# map(functionName, list_to_perform_operation_on )
# print(list(map(lambda num : num*2, numbers)))

# -----------------------------------------------------------------------------------------

numbers = [1,5,3,4,1,6,7,2,8,5,10]

# wap to find the cube of each element
print(list(map(lambda num: num**3, numbers)))

# wap to filter the odd numbers
odd = list(filter(lambda num: num%2 != 0, numbers))
print(odd)

# wap to find the product of all numbers using reduce
import functools
print(functools.reduce(lambda num1, num2 : num1*num2, odd))