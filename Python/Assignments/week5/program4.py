positive_sum = 0

numbers = list(map(int, input('Enter numbers (space seperated) : ').split()))

for i in numbers:
    if i <= 0:
        continue
    positive_sum += i

print(positive_sum)