import pandas as pd

arr1 = pd.Series([4,5,6,7,1,3])
arr2 = pd.Series([4,1,2,3,4])

# ARITHMETIC OPERATIONS

# b = arr1.add(arr2)
# print(b)
# NaN - Not a Number

# c = arr1.subtract(arr2)
# print(c)

# d = arr1.multiply(arr2)
# print(d)

# e = arr1.divide(arr2)
# print(e)


# COMBINING SERIES INTO ONE
# append
# arr3 = arr1._append(arr2)
arr3 = arr1._append(arr2, ignore_index=True)
print(arr3)