# 1)A triangle can be classified based on the lengths of its sides as equilateral, isosceles or scalene.
# All three sides of an equilateral triangle have the same length. An isosceles triangle has two sides that are the same length,
# and a third side that is a different length. If all of the sides have different lengths then the triangle is scalene.
# Write a program that reads the lengths of the three sides of a triangle from the user. Then display a message that states the triangle's type,
# also need to find the area of the triangle in python.
import math

side1 = int(input('Side1 : '))
side2 = int(input('Side2 : '))
side3 = int(input('Side3 : '))
type_triangle = ''
area = 0

if side1 == side2 == side3:
    type_triangle = 'Equilateral Triangle'
    area = (math.sqrt(3)/4) * side1**2  # Area of Equilateral Triangle

elif side1 == side2 or side2 == side3 or side1 == side3:
    type_triangle = 'Isosceles Triangle'
    if side1 == side2:
        area = 0.5 * side3 * math.sqrt(side1**2 - ((side3**2)/4))
        # area =
    elif side2 == side3:
        area = 0.5 * side1 * math.sqrt(side2**2 - ((side1**2)/4))
        # area
    elif side1 == side3:
        area = 0.5 * side2 * math.sqrt(side1**2 - ((side2**2)/4))
        
elif side1!= side2 !=side3:
    type_triangle = 'Scalene'
    # Heron's formula
    perimeter = side1 + side2 + side3
    S = perimeter/2
    area = math.sqrt(S*(S - side1)*(S - side2)*(S - side3))

print(f'Area of given {type_triangle} triangle is {round(area,2)}')