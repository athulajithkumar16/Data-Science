
options = int(input('''1. Convert Celsius to Fahrenheit \n2. Convert Fahrenheit to Celsius \n3. Convert Kelvin to F/C \nEnter option(1/2/3) : '''))

if options == 1:
    celsius = float(input('Celsius : '))
    fahrenheit = celsius * (9/5) + 32
    print(fahrenheit, f'{celsius+273.15} K')

elif options == 2:
    fahrenheit = float(input('Fahrenheit : '))
    celsius = ( fahrenheit - 32 ) / (9/5)
    print(celsius, f'{celsius+273.15} K')

elif options == 3:
    kelvin = float(input('Kelvin : '))
    print(f'{round(kelvin-273.15,2)} C', f'{round(kelvin*(9/5)-459.67,2)} F')      
    