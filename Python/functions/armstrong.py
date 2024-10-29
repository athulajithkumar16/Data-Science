def is_armstrong(num):
    dummy = num
    sum = 0
    while num > 0:
        last_digit = num % 10
        sum += last_digit**len(str(dummy))
        num //= 10
        
    if dummy == sum:
        return 'ARMSTRONG'
    else:
        return 'NOT ARMSTRONG'

print(is_armstrong(153))
