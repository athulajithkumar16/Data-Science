# Write a Python program to check if a given string is a valid identifier or not. 
# An identifier is valid if it starts with a letter (a-z, A-Z) or an underscore (_) 
# followed by zero or more letters, underscores, or digits (0-9).

def is_identifer(string):
    if not (string[0].isalpha() or string[0] == '_'):
        return False
    for i in string[1:]:
        if not (i.isalnum() or i == '_'):
            return False
    else:
        return True

# _hello23

string = input('Enter a string : ')
print(is_identifer(string))