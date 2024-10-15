# for rows in range(1,6):
#     for column in range(rows):
#         print(rows, end=' ')
#     print()
# 1  
# 2 2  
# 3 3 3  
# 4 4 4 4  
# 5 5 5 5 5
# ------------------------------------------------------

# for rows in range(1, 6):
#     for column in range(1, rows + 1):
#         print(column, end=' ')
#     print()
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# ------------------------------------------------------


# for row in range(1, 6):
#     for column in range(6-row):
#         print(row, end=' ')
#     print()
# 1 1 1 1 1 
# 2 2 2 2
# 3 3 3
# 4 4
# 5
# ------------------------------------------------------

# SQUARE 
# n = 5
# for i in range(n):
#     for j in range(n):
#         print('*', end=' ')
#     print()

# * * * * * 
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# ------------------------------------------------------

# INCREASING *
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print('*', end=' ')
#     print()

# * 
# * *
# * * *
# * * * *
# * * * * *
# ------------------------------------------------------

# DECREASING *
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print('*', end=' ')
#     print()
# * * * * * 
# * * * *
# * * *
# * *
# *
# ------------------------------------------------------

# RIGHT TRIANGLE
n = 5
for i in range(n):
    for j in range(i, n):
        print(' ', end= ' ')
    for j in range(i+1):
        print('*', end= ' ')
    print()
#           * 
#         * *
#       * * *
#     * * * *
#   * * * * *
# ------------------------------------------------------


# RIGHT SIDED TRIANGLE
# n = 5
# for i in range(n):
#     for j in range(i):
#         print(' ', end=' ')
#     for j in range(n-i):
#         print('*', end=' ')
#     print()
# * * * * *
#   * * * * 
#     * * *
#       * *
#         *

# ====================================================================
n = 5
# SQUARE 
# for i in range(n):
#     for j in range(n):
#         print('*', end=' ')
#     print()

# INCREASING *
# for i in range(n):
#     for j in range(i+1):
#         print('*', end=' ')
#     print()

# DECREASING *
# for i in range(n):
#     for j in range(i, n):
#         print('*', end=' ')
#     print()

# RIGHT TRIANGLE
# for i in range(n):
#     for j in range(i, n-1):
#         print(' ', end=' ')
#     for j in range(i+1):
#         print('*', end=' ')
#     print()

# RIGHT SIDED TRIANGLE
# for i in range(n):
#     for j in range(i):
#         print(' ', end=' ')
#     for j in range(i, n):
#         print('*', end =' ')
#     print()

# HILL PATTERN
# for i in range(n):
    # for j in range(i,n-1):
    #     print(' ', end=' ')
    # for j in range(i+1):
    #     print('*', end=' ')
    # for j in range(i):
    #     print('*', end=' ')
    # print()

# REVERSE HILL
# for i in range(n):
#     for j in range(i):
#         print(' ', end=' ')
#     for j in range(i,n):
#         print('*', end=' ')
#     for j in range(i, n-1):
#         print('*', end=' ')
#     print()

# DIAMOND
# for i in range(n-1):
#     for j in range(i, n-1):
#         print(' ', end=' ')
#     for j in range(i+1):
#         print('*', end=' ')
#     for j in range(i):
#         print('*', end=' ')
#     print()
# for i in range(n):
#     for j in range(i):
#         print(' ', end=' ')
#     for j in range(i, n-1):
#         print('*', end=' ')
#     for j in range(i, n):
#         print('*', end=' ')
#     print()
