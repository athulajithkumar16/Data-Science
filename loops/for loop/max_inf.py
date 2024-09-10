numbers = [10, 20, 4, 45, 99]

max_ = float('-inf')

for i in numbers:
    if max_ < i:
        max_ = i

print(max_)