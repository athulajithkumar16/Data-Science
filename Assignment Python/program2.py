# Write a Python program to find all the valid identifiers in a given string. 
# Assume that identifiers are separated by spaces.

def is_identifer(string):
    if not (string[0].isalpha() or string[0] == '_'):
        return False
    for i in string[1:]:
        if not(i.isalnum() or i == '_'):
            return False
    else:
        return True

identifiers = list(map(str, input('Enter identifers : ').split()))

for i in identifiers:
    if is_identifer(i):
        print(f'{i} is valid')
    else:
        print(f'{i} is invalid')