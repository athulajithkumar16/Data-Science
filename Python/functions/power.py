def power(num,pow=2):
    return num**pow

number = int(input('Enter number : '))
# powerr = int(input('Enter power : ')) or 2
powerr = input('Enter power : ')

# print(power(number,pow=3))
if powerr=='':
    print(power(number))
else:
    print(power(number, int(powerr)))