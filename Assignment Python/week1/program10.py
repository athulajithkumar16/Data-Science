# Write a function to calculate the factorial of a number recursively.

def fact(num):  # 4 
    if num == 1:
        return num
    else:
        return num * fact(num-1)
                # 4 * 6
                # 3 * 2
                # 2 * 1


number = int(input())
print(fact(number))