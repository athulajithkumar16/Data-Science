# Write a function to calculate the factorial of a number recursively.

def fact(num):
    if num == 1:
        return num
    else:
        return num * fact(num-1)

number = int(input())
print(fact(number))