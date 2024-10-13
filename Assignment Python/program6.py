# Write a Python program that takes two numbers as input from the user and 
# performs arithmetic operations (addition, subtraction, multiplication, division, and modulus) 
# on them. Display the results of each operation.

add = lambda num1, num2 : num1 + num2
sub = lambda num1, num2 : num1 - num2
mult = lambda num1, num2 : num1 * num2
div = lambda num1, num2 : num1 / num2
mod = lambda num1, num2 : num1 % num2

num1 = int(input('Enter first number : '))
num2 = int(input('Enter first number : '))

print(add(num1, num2))
print(sub(num1, num2))
print(mult(num1, num2))
print(div(num1, num2))
print(mod(num1, num2))