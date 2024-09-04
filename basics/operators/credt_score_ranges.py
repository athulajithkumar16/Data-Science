score = int(input('Enter Credit Score Ranges : '))

if score < 580:
    print('Poor')
elif score >= 580 and score < 670:
    print('Fair')
elif score >= 670 and score < 740:
    print('Good')
elif score >= 740 and score < 800:
    print('Very Good')
elif score > 800:
    print('Exceptional')
else:
    print('Invalid Input')