# 5) Given an integer n, return True if n is within 10 of either 100 or 200

def check_range(num):
    return True if num in range(90,111) or num in range(190,211) else False

number = int(input('Enter a number : '))
print(check_range(number))