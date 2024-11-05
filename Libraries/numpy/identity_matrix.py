# IDENTITY matrix   / eye
# [1 0 0]
# [0 1 0]
# [0 0 1]

import numpy as np

arr = np.identity(3, dtype=int)
print(arr)

arr = np.identity(2, dtype=int)
print(arr)

arr = np.identity(4, dtype=int)
print(arr)

arr = np.eye(3, dtype=int)
print(arr)