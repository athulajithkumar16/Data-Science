import numpy as np

# arr = np.arange(1, 11)
# [ 1  2  3  4  5  6  7  8  9 10]

# # sum()
# sum_arr = np.sum(arr)
# print(sum_arr)

# 2 dimensional sum
arr = np.arange(16).reshape(4, 4)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]
#  [12 13 14 15]]
sum_arr = np.sum(arr)
# print(sum_arr)

# AXIS      axis = 0 [column]       axis = 1 [row]

# # Column wise Sum
# axis_arr = np.sum(arr, axis=0)
# print(axis_arr)

# # Row wise Sum
# axis_arr = np.sum(arr, axis=1)
# print(axis_arr)


# SORT
# array_ = np.array([8, 5, 3, 6, 7, 2, 1, 9, 4])

# # # SORTING in ascending order
# sort_arr = np.sort(array_)      
# print(sort_arr)

# # # SORTING in ascending order
# sort_arr = np.sort(array_)[::-1]
# print(sort_arr)


arr_2 = np.array([[4,5,1,7], [8,4,3,5], [7,9,4,5], [5,8,3,6]])
# [[4 5 1 7]
#  [8 4 3 5]
#  [7 9 4 5]
#  [5 8 3 6]]

# Row wise Sorting
# sort_arr_2 = np.sort(arr_2)
# print(sort_arr_2)
# [[1 4 5 7]
#  [3 4 5 8]
#  [4 5 7 9]
#  [3 5 6 8]]

# # Column wise Sorting
# sort_arr_2 = np.sort(arr_2, axis=0)
# print(sort_arr_2)


# MAX
# arrayy = np.array([5, 3, 2, 1, 8, 9, 7])
# max_ = np.max(arrayy)
# print(max_)

arr_2 = np.array([[4,5,1,7], [8,4,3,5], [7,9,4,5], [5,8,3,6]])

# max_ = np.max(arr_2, axis=1)
# print(max_)

max_ = np.max(arr_2, axis=0)
print(max_)