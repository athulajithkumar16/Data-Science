numbers = [10, 32, 44, 4, 99]

first = second = float('inf')

for i in numbers:
    if i < first:
        second = first
        first = i
    elif first < i < second:
        second = i
print(second)