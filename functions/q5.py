# 5) Given an integer n, return True if n is within 10 of either 100 or 200

def check_range(num):
    return True if num in range(100,200) else False

print(check_range(110))