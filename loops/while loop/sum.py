i, sum = 1,0

while i<=5: 
    sum+=i
    if i<5:
        print(i, end=' + ')
    else:
        print(i,end=' ')
    i=i+1

print(f'= {sum}')
