# 3 Write a program to find greatest number among three numbers

num1, num2, num3 = map(int, input().split())

print(f'{num1}' if num2 < num1 > num3 else f'{num2}' if num1 < num2 > num3 else f'{num3}')