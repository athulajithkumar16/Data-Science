lower_limit = int(input('Enter lower limit : '))
upper_limit = int(input('Enter upper limit : '))
prime = []

for i in range(lower_limit, upper_limit +1):
    for j in range(2, i):
        if i%j == 0:
            print(i)
            break
    else:
        prime.append(i)

print(prime)