marks = int(input('Enter marks : '))

if marks > 80:
    print('A')
elif marks <= 80 and marks > 60:
    print('B')
elif marks <= 60 and marks > 50:
    print('C')
elif marks <= 50 and marks > 45:
    print('D')
elif marks <= 45 and marks > 25:
    print('E')
elif marks <= 25:
    print('F')