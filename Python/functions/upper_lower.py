def oddEvenSum(lower_limit=int(input('Lower limit : ')), upper_limit=int(input('Upper limit : '))):

    odd_sum, even_sum = 0, 0
    for i in range(lower_limit, upper_limit+1):
        if i%2 == 0:
            even_sum += i
        else:
            odd_sum += i
        # even_sum += i if i%2 ==0 else odd_sum += i
    print(f'oddSum = {odd_sum} \nevenSum = {even_sum}')

oddEvenSum()