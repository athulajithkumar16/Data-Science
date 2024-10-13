# Write a program that takes inputs from user and prints the multiplication table 
# of that number

number = int(input())

for i in range(1,11):
    print(f'{i} * {number} = {i*number}')