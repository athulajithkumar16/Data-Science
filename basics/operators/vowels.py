# PROGRAM to find number of vowels in a string
word = input('Enter the word : ')
count = 0
vowels = ['a','e','i','o','u']
for i in word:
    for j in vowels:
        if j == i.lower():
            count+=1
print(f'No. of vowels in {word} is {count}')