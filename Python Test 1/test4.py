number = input('Enter the number : ')
if number.isnumeric() == False:
    print('Not a valid number')

else:
    reverse = number[::-1]
    print(reverse)
    # print(reverse[-1])

    if int(reverse) > 500:
        print('Reversed Number is Greater than 500')
    elif reverse[-1] == '0':
        print('Reversed Number Ends With 0')
    else:
        print('Reversed Number does not meet any condition')

# test = '123FA23'
# print(test.isnumeric())