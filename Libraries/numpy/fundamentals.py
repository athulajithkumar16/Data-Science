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