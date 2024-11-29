import numpy as np

arr_2d = np.array([[4,5,3,2],
                [1,4,6,3],
                [6,2,7,9],
                [2,3,1,0]])

# argsort()
b = np.argsort(arr_2d)     # Row wise
print(b)

c = np.argsort(arr_2d, axis=0)     # Column wise
print(c)

# argmax()
e = np.argmax(arr_2d)
print(e)

f = np.argmax(arr_2d, axis=0)
print(f)

# argmin()
g = np.argmin(arr_2d)
print(g)

h = np.argmin(arr_2d, axis=0)
print(h)