# ERROR HANDLING

# most parent class - object

# exception

# Types of Errors :
# ValueError
# Indentation
# Type Error
# Syntax Error
# ZeroDivisonError

# Exception - base class for error handling in python

# try       - used to contain the doubted code ( through client side)
# except     - used to handle the exception occur in try block
# finally
'''
class Exception:
    try:
        doubtful code 

    except
        # handle
        print(anything)
'''

# WRONG
# num1 = int(input('Enter first number : '))
# num2 = int(input('Enter second number : '))

# print(num1 / num2)
# print('Completed')
# print('Committed')

# CORRECT
# try:
#     num1 = int(input('Enter first number : '))
#     num2 = int(input('Enter second number : '))

#     print(num1 / num2)

# except Exception as e:      # as e ( aliasing )
#     print('Zero Division Not Possible')

# print('Committed')


# [10, 20, 30] - list out of range
list_ = [10, 20, 30]
try:
    i = int(input('Enter index : '))
    print(list_[i])

except Exception as e:
    print(e.args)       # displays all errors in a tuple
                        # args - tuple

except IndexError:
    print('Index out of range')

except ValueError:
    print('ValueError has occured')

print('Statement out of try-except')