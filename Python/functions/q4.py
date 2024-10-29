# 4)Write a function that capitalizes the first and fourth letters of a name

def capitalize(string):

    return string[0].upper() + string[1:3] + string[3].upper() + string[4:]
    # dummy = ''
    # for i in range(len(string)):
    #     if i == 0 or i == 3:
    #         dummy += string[i].upper()
    #     else:
    #         dummy += string[i]
    # return dummy

word = input('Enter a word : ')
print(capitalize(word))