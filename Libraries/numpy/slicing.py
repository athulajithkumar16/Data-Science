import numpy as np

arr = np.arange(1, 21).reshape(4,5)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]]

# arr[ row, column ] 

print(arr[1:3,:2])      # row 1,2 col 0 1

print(arr[:3, 1:4])
print(arr[:3, :2])

print(arr[1::2, :4])

print(arr[::2, 1::2])

print(arr[:4:2, ::2])       # row - 0, 1, 2, 3  col - 0, 3, 5

# Zeroth Row of data
print(arr[0, :])

# Zeroth Column of data
print(arr[:, 0])
