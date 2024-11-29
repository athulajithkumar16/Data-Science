# lst = [1, 3, 5, 4, 3, 5, 6, 7, 9, 7, 5, 4, 8, 9, 10, 7, 5, 4]
# # [1, 5, 3, 9, 4, 10]

# result = [lst[0]]

# for i in range(2, len(lst)):
#     if lst[i-2] < lst[i-1] > lst[i]:
#         result.append(lst[i-1])
#     if lst[i-2] > lst[i-1] < lst[i]:
#         result.append(lst[i-1])
    
# print(result)

# Create a function called biggest_odd that takes a string of numbers and returns the biggest odd number in the list.
# For example, if you pass '23569' as an argument, your function should return 9. Use list comprehension.

def biggest_old(numbers):
    # largest = float('-inf')
    # for i in numbers:
    #     if int(i) > largest and int(i)%2 != 0:
    #         largest = int(i)
    # print(largest)

    return max(int(i) for i in numbers if int(i)%2!=0)

print((biggest_old('235687')))