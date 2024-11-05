# 2d 4 5

# 1. Convert matrices into (5,4)
# 1. Convert matrices into (2, 10)
# 1. Convert matrices into (10, 2)

import numpy as np

arr = np.array([[1,2,3,4],
                [2,3,4,5],
                [4,5,6,7],
                [6,7,8,9],
                [8,6,4,2]])

one = arr.reshape(5,4)
print(one)

print('*'*100)

two = arr.reshape(2,10)
print(two)
print('*'*100)

three = arr.reshape(10, 2)
print(three)