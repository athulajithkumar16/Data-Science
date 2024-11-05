# FULL Matrix

# [3 3 3 3 3 3 3 3]     (8,)

# [5 5 5]
# [5 5 5]
# [5 5 5]       (3, 3)

# [4 4 4 4 4]
# [4 4 4 4 4]
# [4 4 4 4 4]       (3, 5)


import numpy as np

arr = np.full([3, 3], 4)
print(arr)

# One Dimensional
arr = np.full([6], 7)
print(arr)

# Two Dimensional
arr = np.full([5, 4], 6)
print(arr)

# Three Dimensional
arr = np.full([3, 3, 4], 5)
print(arr)