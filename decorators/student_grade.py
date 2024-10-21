'''
Write a class Student with attributes 
name 
marks - dictionary of subjectname and marks

methods 
add_marks(subject, marks)
get_marks(subject)
average_marks()
'''

class Student:

    def __init__(self, name):
        self.name = name
        self.result = {}

    def add_marks(self, subject, marks):
        self.result[subject] = marks
        return self.result
    
    def get_marks(self, subject):
        return self.result[subject]
    
    def average(self):
        average_ = sum(i / len(self.result.keys()) for i in self.result.values())
        return average_
    
student1 = Student(name='Sukumar')
print(student1.add_marks('Maths',90))

student2 = Student(name='Hari')
print(student1.add_marks('Social',85))
# print(student1.get_marks('Social'))

print(student1.average())
