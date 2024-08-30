is_raining = input('Is raining ? ')

if is_raining.lower() == 'yes':
    is_windy = input('Is windy ? ')
    if is_windy.lower() == 'yes':
        print('It is too windy for an umbrella')
    else:
        print('Take an umbrella')
else:
    print('Enjoy your day')