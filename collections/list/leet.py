# input - [1,2,3,4,5]
# output - [1,5,2,4,3]

# head = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# USING WHILE LOOP
# i = 1
# while i <= len(head):
#     head.insert(i, head.pop(-1))
#     i+=2

# print(head)

# USING FOR LOOP
# for i in range(1, len(head), 2):
#     head.insert(i, head.pop(-1))
# print(head)

# QUESTION 2
# INPUT - [1,2,3,4,5]   n=2
# OUTPUT - [1,2,3,5]

# head = [1,2,3,4,5]
# print(head)
# n = int(input('Enter a number : '))
# head.pop(-(n))
# print(head)

# QUESTION 3
# text1 = 'ABC'
# text2 = 'PQR'
# # result = ['A', 'P', 'B', 'Q', 'C', 'R']

# list1 = list(text1)
# list2 = list(text2)

# count = 1

# for i in list2:
#     list1.insert(count, i)
#     count += 2

# print(list1)


# CREATE A NEW LIST
# items = ['apple', 'cherry', 'grape', 'fig', 'BANANA']
# # for i in items:
# #     if 'a' in i.lower():
# #         list1.append(i)

#     # OR
# list1 = [i for i in items if 'a' in i.lower()]
# print(list1)

words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape','ace']
list_ = []
newlist = []

for i in words:
    if 'e' in i.lower() and len(i) > 3:
        # if len(i)**2 % 2 == 0:
        #     newlist.append(len(i)**2)
        list_.append(len(i)**2)

for i in list_:
    if i%2 == 0:
        newlist.append(i)
        
print(words)
print(list_)
print(newlist)