import functools        # reduce

numbers = [1,2,3,4,5,6,7,8]

print(functools.reduce(lambda a,b: a+b, numbers))