# OOPS
# Object Oriented Programming

# Class     - a blueprint for creating objects

'''
list, str, int

# BUILT IN CLASS
class list:
    def append():
        # statements to add an element from the rear

    def pop():
        # statements to delete an element from the rear

These methods can only be called by the 
                                OBJECTS of CLASS <list>


function - normally defined functions 

method - funtions defined in a class        # objectName.methodName()
'''

# Object

# class Students:
#     # method1
#     def greet(self):
#         print(f'Welcome')
# student1 = Students()       # student1 - OBJECT

# print(type(student1))       # <class '__main__.Students'>

# student1.greet()

# -----------------------------------------------
# class Test(Students):
#     def hello():
#         print('Hello WOrld')
# -----------------------------------------------

class Students:

    name : str
    place : str

    def register(self, name, place):
        self.name = name
        self.place = place

    def greet(self):
        print(f'Welcome {self.name}')

    def details(self):
        print(f'Hello {self.name} from {self.place}')

student1 = Students()
student1.register(name='Hari', place='Kochi')

student2 = Students()
student2.register(name='Surya', place='Chennai')

student3 = Students()
student3.register(name='Aravind', place='Palakkad')

student1.greet()
student2.details()
student3.greet()