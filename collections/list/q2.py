'''Given a pattern text=”ABEABAIACB” Write a program to print most recursive
consonant from above text  Output=B'''

text = 'ABEABAIACB'

count = 0
list_ = list(text)

for i in list_:
    if i.lower() not in 'aeiou' and list_.count(i) > count:

        count = list_.count(i)
        element = i

print(element)