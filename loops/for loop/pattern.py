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

for row in range(1,5):
    for column in range(1,5):
        print(column, end='\t')
        if column == row:
            break
    print()