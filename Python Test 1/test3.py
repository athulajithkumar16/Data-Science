string = input('Enter the string : ')
reverse_string = ''
dummy_string = ''

position = string.index('o')

for i in range(position):
    reverse_string += string[i]

for i in range(position,len(string)):
    dummy_string += string[i]

print(reverse_string[::-1] + dummy_string)


