# Example 8: Python program to check if the given string is a palindrome.

string = input('Enter string : ')

reverse_string = ''

for i in string:
    reverse_string = i + reverse_string

if string == reverse_string:
    print('PALINDROME')
else:
    print('NOT PALINDROME')