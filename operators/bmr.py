options = input('M/F : ')
age = int(input('Age : '))
weight = int(input('Weight : '))
height = int(input('Height : '))

if options.lower() == 'm':
    bmr = 88.362 + (13.397 * weight) + (4.799*height) - (5.677*age)
    

elif options.lower() == 'f':
    bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330*age)

print(bmr)