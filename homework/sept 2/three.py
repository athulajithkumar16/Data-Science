# 3)A company decided to give a bonus of 5% to an employee if his/her year of service is more than 5 years.
#  Ask user for their salary and year of service and print the net bonus amount.

salary = int(input('Enter your salary : '))
year_of_service = int(input('Years of service : '))

if year_of_service > 5:
    print(f'Net bonus amount is ₹{salary*(5/100)}')