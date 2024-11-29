import numpy as np

arr = np.array([6,4,7,5, 2, 8, 3,15, 12, 11])

# arr = np.arange(20).reshape(4,5)

# argsort()
b = np.argsort(arr)
# print(b)

# argmax()
c = np.argmax(arr)
# print(c)

for i in arr:
    print(i)