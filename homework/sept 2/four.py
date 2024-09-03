# 4) Write a Python program that validates a license plate based on the following criteria:
#     a) The license plate must be exactly 7 characters long.
#     b) The first three characters must be uppercase letters.
#     c) The last four characters must be digits.
#     d) The license plate must not contain any spaces or special characters.
# The program should print whether the license plate is valid or not, and if not, indicate which condition(s) it failed.

license_plate = input('Enter license plate : ')

if len(license_plate) == 7 and license_plate[:3].isupper() == True and license_plate[-4:].isdigit() == True and ' ' not in license_plate:
    print(f'License plate No. {license_plate} is Valid!')
else:
    print(f'License plate No. {license_plate} is Invalid!')