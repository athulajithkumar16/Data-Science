side1, side2, side3 = map(int, input().split())

if side1 == side2 == side3:
    print('Equilateral Triangle')
elif side1 == side2 or side2 == side3 or side1 == side3:
    print('Isosceles Triangle')
else:
    print('Scalene Triangle')