numbers = list(map(int, input('Enter values : ').split()))

for i in range(len(numbers) - 1):
    if numbers[i+1] - numbers[i] == 2:
        print(f'Missing Number is : {numbers[i+1] - 1}')
        break