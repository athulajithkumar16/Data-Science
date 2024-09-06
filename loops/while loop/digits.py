num = int(input('Enter the number : '))
dummy_num = num

# METHOD 1
count = 0
while num > 0:
    digit = num % 10
    # print(f'Digit : {digit}')
    count += 1 
    # print(f'Count : {count}')
    num = num//10
    # print(f'Number : {num}\n')
print(f'Number of digits in {dummy_num} is {count}')


# METHOD 2
# count = 0
# i = 1
# while i < num:
#     count += 1
#     i *= 10
#     print(i)
# print(f'Number of digits in {dummy_num} is {count}')


# METHOD 3
# print(len(str(num)))