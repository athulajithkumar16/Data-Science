# Example 9: Python program that accepts a word from the user and reverses it.

word = input('Enter a word : ')
reversed_ = ''

for i in word:
    reversed_ = i + reversed_

print(reversed_)