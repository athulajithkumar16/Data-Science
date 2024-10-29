number = int(input('Enter the number : '))
count = 0

# print(str(number)[::-1])
for i in str(number):

    # count += 1 if int(i)%2 != 0 else 
    if int(i) % 2 !=0:
        count+=1
print(count)