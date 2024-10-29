# DECORATORS

def swap_num(function):

    def wrapper(num1, num2):
        if num1 < num2:
            num1, num2 = num2, num1
        return function(num1, num2)
    return wrapper


@swap_num
def subtraction(a, b):
    return a-b

print(subtraction(4,2))
print(subtraction(4,6))

def division(a,b):
    return a/b

print(division(4,2))
print(division(2,4))