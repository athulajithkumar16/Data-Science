def minimum(num1, num2, num3):
    # return min(num1,num2,num3)
    return num1 if num2 > num1 < num1 else num2 if num1 > num2 < num3 else num3
print(minimum(3,5,2)) 