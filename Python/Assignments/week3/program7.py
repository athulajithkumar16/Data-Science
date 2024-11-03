number = int(input('Enter a number : '))
summ = 0

for i in range(1,number):
    if number % i ==0:
        summ += i
print(summ)
if number == summ:
    print('Perfect Number')
else:
    print('Not perfect')