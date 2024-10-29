
price = int(input('Enter price of the bike : '))

if price > 100000:
    print(f'Road tax of the bike is {price*(15/100)}')
elif price >= 50000 and price <= 100000:
    print(f'Road tax of the bike is {price*(10/100)}')
else:
    print(f'Road tax of the bike is {price*(5/100)}')