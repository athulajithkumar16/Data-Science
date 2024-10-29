# Given a pattern Text=”ABABC”
# Write a program to print first non-recursive character output=c without
# using nested loop

text = 'ABABDC'

list_ = list(text)

for i in list_:
    if list_.count(i) == 1:
        print(i)
        break