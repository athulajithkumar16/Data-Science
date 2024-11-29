import numpy as np

arr = np.array([6,4,7,5, 2, 8, 3,15, 12, 11, 1, 20])

# search ===> where

b = np.where(arr==2)
# print(b)


arr_2d = np.array([[4,5,3,2],
                [1,4,6,3],
                [6,2,7,9],
                [2,3,1,0]])

c = np.where(arr_2d>5)
print(c)