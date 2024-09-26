'''
    args and kwargs takes the input values into a collection

    Args is TUPLE
    KWargs is DICTIONARY 
'''

def sum_num(*args):
    sum = 0
    print(args)         # TUPLE
    for i in args:
        sum += i
    return sum
# OR 
# sum_num = lambda *args : sum(args)
# print(sum_num(1,2,3,4,5,5))


def details(**kwargs):      # KEYWORD ARGUMENTS
    print(kwargs)           # DICTIONARY

details(name='Athul', rollno=52)
details(name='Aalfin', rollno=23)


