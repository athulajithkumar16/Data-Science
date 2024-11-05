import numpy as np

# Reshape       -   to change the order of the matrix we created
# (3,4) =====> (4,3)
# (5,4) =====> (4,5)

a = np.array([[1,2,3,4], 
              [2,3,4,5],
              [5,6,7,8]])       # 3 x 4

b = a.reshape(4,3)          # 4 x 3
print(b)

c = a.reshape(2, 6)          # 2 x 6
print(c)

'''
Can change the shape of the matrix using reshape() but 
    the order of the matrix must be same.
'''