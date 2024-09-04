num = int(input('Enter a number : '))

print("Divisible by both 3 and 5" if num%3==0 and num%5==0 else ("Divisible by either 3 or 5" if num%3==0 or num%5==0 else "Not divisible by 3 or 5"))


