import numpy as np

arr = np.array([1,5,7,8,9,15,20,25,30,35,40,25])

# filter


for i in arr:
    if i%2 == 0:
        print(i)