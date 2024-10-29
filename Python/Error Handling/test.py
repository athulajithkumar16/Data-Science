# 1)Write a Python program that:

# Asks the user for a filename to read.
# If the file exists, it reads and prints the content of the file.
# If the file does not exist, it should catch the exception and create a new file with the specified name. 
# The program should then write a default message, "New file created.", to the file.

# try:
#     file_name = input('Enter file name : ')
#     with open(file_name, 'r') as file:
#         content = file.read()
#         print("File content:")
#         print(content)

# except FileNotFoundError:
#     print("FileNotFoundError")
#     with open(file_name, 'w') as file:
#         file.write("New file created.")

# except FileExistsError:
#     print(f"'{file_name}' already exists.")


# 2)Takes a list of numbers as input from the user (all numbers entered in a single line, separated by spaces).
# Calculate the sum of even-indexed numbers (i.e., elements at index 0, 2, 4, etc.) and the sum of odd-indexed numbers (i.e., elements at index 1, 3, 5, etc.).
# Then, without using any conditions (if), return the difference between the sum of even-indexed and odd-indexed numbers.

# numbers = [int(i) for i in input('Enter numbers : ').split()]
# sum_even_index, sum_odd_index = 0, 0

# for i in range(len(numbers)):
#     if i % 2 == 0:
#         sum_even_index += numbers[i]
#     else:
#         sum_odd_index += numbers[i]

# print(abs(sum_even_index-sum_odd_index))        # use decorators

# 3)Write a Python program that:

# Defines a class Library with a dictionary attribute books where the keys are book titles and the values are the number of copies available.
# The class should have the following methods:
# add_book(title, copies): Adds a new book to the dictionary or updates the number of copies if the book already exists.
# borrow_book(title): Reduces the number of copies by 1 if the book is available (no condition allowed, handle it through logical operations).
# return_book(title): Increases the number of copies by 1 when a book is returned.

class Library:

    def __init__(self):
        self.books = {}

    def add_book(self, title, copies):
        self.books[title] = int(copies)

    def borrow_book(self, title):
        if title in self.books.keys():
            self.books[title] -= 1

    def return_book(self, title):
        if title in self.books.keys():
            self.books[title] += 1


student1 = Library()
student1.add_book('Basheer', 3)
student1.add_book('And the mountains echoed', 2)

student1.borrow_book('Basheer')