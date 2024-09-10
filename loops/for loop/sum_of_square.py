# SUM OF SQUARE OF EVEN DIGITS IN A NUMBER

number = 123456789
sum = 0

for i in str(number):
    if int(i)%2 == 0:
        sum += int(i)**2  # 2^2 + 4^2 + 6^2 + 8^2

print(sum)