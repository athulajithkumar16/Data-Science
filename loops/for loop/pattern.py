# print('good', end='')
# print('morning')

# for i in range(5):
#     print(i, end=' ')

# string = 'abcedfghijklmno'
# print(string[-1])

# for i in range(5,0,-1):
#     print(i,end='@')

# for i in range(5,-1,-1):
#     print(i,end=' @ ')

# for i in range(1,5):
#     for j in range(1,5):
#         print(j, end=' ')
#     print()

# for row in range(5):
#     for column in range(4):
#         print('*', end='\t')
#     print()

# for row in range(1,5):
#     for column in range(1,row+1):
#         print(column, end='\t')
#         if column == row:
#             break
#     print()

# for row in range(3):
#     for column in range(3):
#         print('*', end='\t')
#         if column == row:
#             break
#     print()

# for row in range(3):
#     for column in range(row+1):
#         print('*', end='\t')
#         # if column == row:
#         #     break
#     print()

for row in range(1,5):
    for column in range(1,row+1):
        print(row, end=' ')
    print()
# 1
# 2 2
# 3 3 3
# 4 4 4 4 