# wap to print sum of even and odd indexed digits in a given number

num = 14263
odd_sum, even_sum = 0, 0

for i in range(len((str(num)))):
    if i%2 == 0:
        even_sum += int(str(num)[i])
    else:
        odd_sum += int(str(num)[i])

print(f'Odd Sum : {odd_sum} \nEven Sum : {even_sum}')
