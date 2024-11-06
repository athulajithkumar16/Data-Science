import numpy as np

arr = np.arange(1,10).reshape(3,3)
        # [1,2,3]
        # [4,5,6]
        # [7,8,9]

brr = np.arange(9, 0, -1).reshape(3,3)
        # [9,8,7]
        # [6,5,4]
        # [3,2,1]

# Addition                  # element by element addition
c = np.add(arr, brr)        # ORDER must be same of both arrays
# print(c)                

# Subtraction               # element by element subtraction
d = np.subtract(arr,brr)
# print(d)

# Multiplication
mul = np.multiply(arr, brr)     #dot product    # element by element multiplication
# print(mul)

# Divide
div = np.divide(arr, brr)       # element by element division
# print(div)

# Square()
sq = np.square(arr)
# print(sq)

# sqrt()
squareRoot = np.sqrt(arr)
# print(squareRoot)

# Dot product       
'''
[3 4 5]     [4 5 6]         dot product - [3*4+4*4+5*4  3*5+4*1+5*7  3*6+4*2+5*8]
[1 2 3]     [4 1 2]                       [1*4+2*4+3*4  1*5+2*1+3*2  1*6+2*1+3*2]  
[6 5 4]     [4 7 8]                       [6*4+5*4+4*4  6*5+5*1+4*7  6*6+5*2+4*8]                 
'''
# # first matrix number of columns = second matrix number of rows

arr = np.array([[3,4,5], [1,2,3], [6,5,4]])
brr = np.array([[4,5,6], [4,1,2], [4,7,8]])

dotproduct = np.dot(arr, brr)
# print(dotproduct)

# Slicing
arr = np.arange(20)
print(arr)
print(arr[2])
print(arr[7])
print(arr[1:4])
print(arr[3:6])
print(arr[3:])
print(arr[:5])
print(arr[1:7:2])
print(arr[1::3])
print(arr[:8:3])
print(arr[::4])