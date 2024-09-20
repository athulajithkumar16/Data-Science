first, second = 0, 1
sum = 0
print(first, second, end=' ')
for i in range(100):
    sum = first + second
    first, second = second, sum
    print(sum, end=' ')