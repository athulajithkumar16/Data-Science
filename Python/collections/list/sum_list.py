list_ = [1,2,9,65,4,3,7,6]      # sum of square of even numbers
sum = 0

for i in list_:
    if i%2 == 0:
        sum += i**2
print(sum)