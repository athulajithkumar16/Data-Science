numbers = [10, 20, 4, 45, 99]

min_ = float('inf')
for i in numbers:
    if min_ > i:
        min_ = i
print(min_)