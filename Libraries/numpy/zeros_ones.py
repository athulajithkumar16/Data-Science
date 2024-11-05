# Zero Matrix

import numpy as np

# arr = np.zeros([3,3], dtype=int)
# print(arr) 

# arr = np.zeros([1, 5,4], dtype=int)
# print(arr) 

# arr = np.ones([3,3], dtype=int)
# print(arr) 

# arr = np.zeros([2, 4, 4], dtype=int)
# print(arr)                              # prints 4x4 zero matrix 2 times

# arr = np.zeros([3, 4, 4], dtype=int)
# print(arr)                              # prints 4x4 zero matrix 3 times
# print(arr.size)     # 3 * 4 * 4

# [1 1 1]
# [1 1 1]       (2x3)

# [1 1 1 1]
# [1 1 1 1]
# [1 1 1 1]     (3x4)

# [1 1 1 1 1]   (5,)

# # ONE Dimensional
# arr = np.ones([5], dtype=int)
# print(arr)

# # TWO Dimensional
# arr = np.ones([3, 4], dtype=int)
# print(arr)

# THREE Dimensional
arr = np.ones([3, 4, 4], dtype=int)
print(arr)