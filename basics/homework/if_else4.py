
# Write a Python program that asks the user to enter an integer and then classifies the number based on the following criteria:
# Divisible by 2 and 3: Print "The number is divisible by both 2 and 3."
# Divisible by 2 but not by 3: Print "The number is divisible by 2 but not by 3." 
# Divisible by 3 but not by 2: Print "The number is divisible by 3 but not by 2.
# Not divisible by either 2 or 3: Print "The number is not divisible by either 2 or 3."

integer = int(input('Enter an integer : '))

if integer % 2 == 0 and integer % 3 == 0:
    print('The number is divisible by both 2 and 3.')
elif integer % 2 == 0 and integer % 3 != 0:
    print('The number is divisible by 2 but not by 3')
elif integer % 3 == 0 and integer % 2 != 0:
    print('The number is divisible by 3 but not by 2.')
else:
    print('The number is not divisible by either 2 or 3.')