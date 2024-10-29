# def second_largest(lst):
#     first = second = float('-inf')
#     for num in lst:
#         if num > first:
#             second = first
#             first = num
#         elif first > num > second:
#             second = num
#     return second

numbers = [10, 20, 4, 45, 99]
first = second = float('-inf')
for i in numbers:
    if i > first:
        second, first = first, i
    elif first > i > second:
        second = i

print(second)