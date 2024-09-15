# Example 11: Python program to count the number of even and odd numbers from a series of numbers.

num = list(map(int,input('Enter series of numbers : ').split()))
#  [1,3,5,6,99,134,55]
even, odd = 0, 0

for i in num:
    if i % 2 == 0:
        even+=1
    else:
        odd+=1

print(f'{even} EVEN \n{odd} ODD')