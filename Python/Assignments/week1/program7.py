# Create a Python program that prompts the user to enter two numbers. 
# Compare the numbers using comparison operators (>, <, ==, !=, >=, <=) 
# and print out the result of each comparison.

num1 = int(input())
num2 = int(input())

print(num1 if num1 > num2 else num2)
print(num1 if num1 < num2 else num2)
print(num1 if num1 == num2 else num2)
print(num1 if num1 != num2 else num2)
print(num1 if num1 >= num2 else num2)
print(num1 if num1 <= num2 else num2)