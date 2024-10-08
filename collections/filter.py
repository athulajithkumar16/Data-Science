# FILTER
# filter( function_to_perform, collection_to_workout_on )

# numbers = [1,2,3,4,5,6,7,8]
# print(list(filter(lambda num : num % 2 == 0, numbers)))


numbers = [1,5,3,4,15,6,7,20,28,35,10]

odd = list(filter(lambda num: num%2 !=0, numbers))  # taking odd ones out of the list
print(odd)

square = list(map(lambda num: num**2, odd))     #taking the square of each element
print(square)