import numpy as np

arr = np.array([[1,2,3,4],
                [2,3,4,5],
                [4,5,6,8]])

a = arr.reshape(4,3)
print(a)
b = arr.reshape([1,2,6])
print(b)

c = arr.reshape(12)
print(c)