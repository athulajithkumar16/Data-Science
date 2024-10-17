# Parent1, Parent2 still inherits < class object > 
# < class object > is the base class of all classes

'''Types of Inheritance :
    1. Single Inheritance
    2. Multiple Inheritance
    3. Multilevel Inheritance
    4. Hierarchical Inheritance
    5. Hybrid Inheritance
'''

# # SINGLE INHERITANCE

# class Parent1:
#     def method1(self):
#         print('Parent1')

# class Parent2:
#     def method2(self):
#         print('Parent2')

# class Child(Parent1):
#     def method3(self):
#         print(f'I am the child')

# object1 = Child()
# object1.method1()
# object1.method2()
# object1.method3()

# ------------------------------------------------------------
# # MULTI LEVEL INHERITANCE

# class P1:
#     def method1(self):
#         # print('I am the parent')
#         return 'test'

# class Child1(P1):
#     def method2(self):
#         print('I am the Child1')

# class Child2(Child1):
#     def method3(self):
#         print('I am the Child2')

# object1 = Child2()
# object1.method1()
# object1.method2()
# object1.method3()

# ------------------------------------------------------------
# # MULTIPLE INHERITANCE

# class Parent1:
#     def method1(self):
#         return 'Parent1'

# class Parent2:
#     def method2(self):
#         return 'Parent2'

# class Child(Parent1, Parent2):
#     def method3(self):
#         print(f'I am the child of {self.method1()} and {self.method2()}')

# object1 = Child()
# print(object1.method1())
# print(object1.method2())
# object1.method3()

# ------------------------------------------------------------

# Java doesn't support Multiple Inheritance
# It shows error known as 'AMBIGUITY'
# method they used to resolve this - Interface

# ------------------------------------------------------------
# class Parent1:
#     def method1(self):
#         return 'Method1'

# class Parent2:
#     def method1(self):
#         return 'Method2'

# class Child(Parent1, Parent2):
#     def method3(self):
#         print(f'I am the child of {self.method1()} and {self.method2()}')

# object1 = Child()

# print(object1.method1())    # Method1 - since Child class has Parent1 inheriting first, they execute by the order and returns first

# -----------------------------------------------------------------------------------------------------------

# # Method Overloading
# # Two or more methods have the same name but
# # different numbers of parameters or different types of parameters, or both.
# class Sum:
#     def add(self, a, b):
#         self.a = a
#         self.b = b
#         return a + b
    
#     def add(self, x, y, z):
#         self.x = x
#         self.y = y
#         self. z = z
#         return x + y + z
        
# object1 = Sum()

# print(object1.add(2,3))
# print(object1.add(2,3,5))
# ------------------------------------------------------------

# Method Overloading Solved
class Sum:
    def add(self, *args):
        return sum(args)
object1 = Sum()

print(object1.add(2,3))
print(object1.add(2,3,5))

# Method Overloading is solved using None       (NOT *args)