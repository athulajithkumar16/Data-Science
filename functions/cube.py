# RETURN CUBE OF A NUMBER IF NUMBER IS ODD ELSE RETURN SQUARE OF THE NUMBER

cube = lambda num : num**3 if num % 2 != 0 else num **2

print(cube(3))
print(cube(4))