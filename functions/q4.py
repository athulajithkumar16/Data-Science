# 4)Write a function that capitalizes the first and fourth letters of a name

def capitalize(string):
    dummy = ''
    for i in range(len(string)):
        if i == 0 or i == 3:
            dummy += string[i].upper()
        else:
            dummy += string[i]
    return dummy

word = input('Enter a word : ')
print(capitalize(word))