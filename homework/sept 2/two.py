# 2)A shop will give a discount of 10% if the cost of the purchased quantity is more than 1000. 
# Ask the user for quantity, suppose, one unit will cost 100. Judge and print total cost for user

one_unit = 100
quantity = int(input('Please enter the quantity : '))
total_price = one_unit * quantity
print(total_price)

if quantity > 1000:
    print(f'Total price after 10% discount : ₹{total_price*(10/100)}')

else:
    print(f'Total price : ₹{total_price}')
