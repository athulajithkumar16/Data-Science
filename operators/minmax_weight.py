bmi_max = 24.9
bmi_min = 18.5
height = int(input('Enter your height(in cm) : '))

max_weight = bmi_max * (height/100)**2
min_weight = bmi_min * (height/100)**2


print('Max Weight : ',round(max_weight,2))
print('Min Weight : ',round(min_weight,2))