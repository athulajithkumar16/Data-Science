import numpy as np

arr = np.array([[1,2,3], [4,5,6]])

print(arr)

print(arr.ndim)     # No of dimensions

print(arr.shape)    # Order of array

print(arr.size)     # Total number of elements in array

print(arr.dtype)    # data type of array

arr = np.zeros([3,3], dtype=int)

arr = np.ones([3,3], dtype=int)