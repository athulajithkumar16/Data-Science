# Write a Python program to generate all possible valid identifiers of length n, 
# where n is provided by the user. Also take n values from user. Then create possible identifiers
from itertools import combinations
n = int(input())

# VALID IDENTIFIERS
def possible_identifiers(length):
    caps = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    small = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    underscore = ['_']
    first = caps + small + underscore
    digits = [str(i) for i in range(10)]
    test = ''

    for i in combinations(first, 1):
        test += ''.join(i)
        if not test[0].isnumeric():

            for j in combinations(first + digits, length ):                
                    test += ''.join(j)
                    print(test)
                    test = ''

possible_identifiers(n)