# wap to print the characters of a string in even positions. 
# >>>      name= "python"    o/p = y h n

string = 'python'

for i in range(len(string)):
    if i % 2 != 0:
        print(string[i], end=' ')