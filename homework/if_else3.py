
# Write a Python program that asks the user to enter their age and then determines the price of a movie ticket based on the following age groups:
# Under 3 years old: Free
# 3 to 12 years old: rs10
# 13 to 59 years old: rs15
# 60 years and older: rs12

age = int(input('Enter your age : '))
if age <= 0 :
    print('Invalid Input')
elif age <= 3:
    print('Free')
elif age > 3 and age <= 12 :
    print('Please pay ₹10')
elif age > 12 and age < 60:
    print('Please pay ₹15')
elif age >= 60:
    print('Please pay ₹12')
