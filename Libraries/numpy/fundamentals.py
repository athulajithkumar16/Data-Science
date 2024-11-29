import numpy as np

arr = np.array([[1,2,3], [4,5,6]])

print(arr)

print(arr.ndim)     # No of dimensions

print(arr.shape)    # Order of array

print(arr.size)     # Total number of elements in array

print(arr.dtype)    # data type of array

arr = np.zeros([3,3], dtype=int)

arr = np.ones([3,3], dtype=int)

arr = np.ones([2, 3,3], dtype=int)

# Full Matrix
arr = np.full([3, 3], 4)

# Identity Matrix
arr = np.identity(3, dtype=int)

# Complex Matrix
arr = np.array([3, 4, 5, 6, 7, 8], dtype=complex)

# Reshape
a = np.array([[1,2,3,4], 
              [2,3,4,5],
              [5,6,7,8]])       # 3 x 4

b = a.reshape(4,3)          # 4 x 3
b = a.reshape(2, 3, 2)          # 2 x 3 x 2

c = arr.flatten()       # converts array into 1 dimension

arr = np.arange(9, 101)     # arange() - to get a range of values in array

arr = np.arange(1,21).reshape(1,5,4)

arr = np.linspace(1,25, 6)      # start, stop, number of elements
        # Return evenly spaced numbers over a specified interval

# Arithmetic Operations
    # Addition
arr = np.add(a, b)
arr = np.subtract(a, b)
arr = np.multiply(a, b)
arr = np.divide(a, b)
arr = np.square(a)
arr = np.sqrt(a)

dotproduct = np.dot(a,b)

# Slicing
print(arr[1::2, :4])

# Built in functions
# sum()
sum_arr = np.sum(arr)

axis_arr = np.sum(arr, axis=0)        # column wise sum (axis = 0)
axis_arr = np.sum(arr, axis=1)        # row wise sum (axis = 1)

# SORTING
sort_arr = np.sort(arr)      
sort_arr = np.sort(arr)[::-1]      

axis_arr = np.sort(arr, axis=0)        # column wise sort (axis = 0)
axis_arr = np.sort(arr)                # default row wise sort (axis = 1)
