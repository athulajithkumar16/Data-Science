list_ = [0,1,2,3,4,5,6,7,8,9]
print(list_)

swap1 = int(input('Enter a position to swap :'))
swap2 = int(input('Enter another position to swap :'))

list_[swap1], list_[swap2] = list_[swap2], list_[swap1]

print(list_)
