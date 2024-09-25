# Write a Python function area(length, width) that calculates the area of a rectangle.
# If only the length is provided, the function should return the area of a square
# (assuming length = width). If both length and width are provided, it should return
# the area of the rectangle

def area(length, width=None):

    return length*width if width != None else length*length

lengthh = int(input('Length : '))
widthh = input('Width : ')

if widthh=='':
    print('test')

# print(area(lengthh, widthh))

# def area(dum_length, dum_width):
#     return dum_length*dum_width
# length = int(input('Enter length : '))
# width = input('Enter width : ')
# if width=='':
#     width = length
# print(area(length,int(width)))