name = 'Athena'
list_name = list(name)

# print(list_name)

list_ = []
# print(type(list_))      # <class 'list'>

list2 = ['suku', 12, 13, [1, 2, 3, 'alfin'],19]

# list2.append(20)         

# print(list2)        # ['suku', 12, 13, [1, 2, 3, 'alfin'], 20]

list2.pop()   
print(list2.pop())      # remove and return item at index

list2.pop(1)     # remove and return item at index
# print(list2)

list2.insert(2,True)
# print(list2)

text = 'ABEABAIACB'
list_ = list(text)

# clear()
# copy()
# remove()
# reverse()

# print(list_.clear())      # None
# print(list_.copy())     #  ['A', 'B', 'E', 'A', 'B', 'A', 'I', 'A', 'C', 'B']
# list_.remove('A')           # Remove first occurrence of the value 
# print(list_)
list_.reverse()             # Reverse the list
print(list_)                # ['B', 'C', 'A', 'I', 'A', 'B', 'A', 'E', 'B', 'A']