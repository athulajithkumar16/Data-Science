import numpy as np

arr = np.array([[1,2,3,4], [3,4,5,6], [4,5,6,7], [6,7,8,9]])    #   4 x 4

# 3 dimensional (2, 8)
a = arr.reshape(1,2,8)
print(a)

# 1 dimensional
b = arr.reshape(16)
print(b)

# flatten()

c = arr.flatten()
print(c)