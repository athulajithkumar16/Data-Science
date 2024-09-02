height = int(input('Height(cm) :'))
weight = int(input('Weight(kg) :'))

bmi = weight / (height/100)**2 
print(bmi)

if bmi < 18.5 and bmi > 0:
    print('Underweight !!')
elif bmi > 18.5 and bmi < 24.9:
    print('Normal Weight')
elif bmi > 25 and bmi < 29.9:
    print('Overweight !!')
else: 
    print('Obese !!')