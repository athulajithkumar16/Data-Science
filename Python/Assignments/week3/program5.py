size = int(input('Enter range : '))

for num in range(size):
    if num == 1:
        print(num, end=' ')
    else:
        for i in range(2, num):
            if num % i == 0:
                break
            else:
                print(num, end=' ')