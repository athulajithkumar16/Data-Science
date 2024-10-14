# 5. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user.

quantity = int(input('Enter quantity : '))
cost = quantity * 100

print(f'Cost is  ₹{cost*(90/100)} after discount' if quantity > 1000 else f'Cost is  ₹{cost}')