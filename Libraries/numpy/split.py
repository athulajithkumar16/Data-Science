import numpy as np

arr = np.array([6,4,7,5, 2, 8, 3,15, 12, 11, 1, 20])

# split

b = np.split(arr, 3)
print(b)        # [array([6, 4, 7, 5]), array([ 2,  8,  3, 15]), array([12, 11,  1, 20])]

for i in b:
    print(i)