# Write a program to 

try:
    file = open('example.txt')
    print(file.read())
    file.close()

except Exception as e:
    print(e.args)
except FileNotFoundError:
    print('FileNotFoundError exists')

finally:
    print('Hello world anws')