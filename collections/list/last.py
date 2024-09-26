nums = [1,2,9,65,4,3,7,6]

for i in range(3):
    last = nums.pop()
    nums.insert(0,last)

print(nums)