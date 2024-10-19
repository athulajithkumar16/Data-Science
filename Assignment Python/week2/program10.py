def check_square(length, breadth):
    if length == breadth:
        return True
    else:
        return False
    
length = int(input('Length : '))
breadth = int(input('Breadth : '))

print(check_square(length, breadth))