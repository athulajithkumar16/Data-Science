
num = int(input('Enter the number : '))
dummy_num = num
count = 0

while num > 0:

    digit = num % 10
    # print(f'Digit : {digit}')

    count += 1 
    # print(f'Count : {count}')

    num = num//10
    # print(f'Number : {num}\n')

print(f'Number of digits in {dummy_num} is {count}')