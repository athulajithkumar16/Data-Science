class Employee:

    def __init__(self,name,role,place):     # CONSTRUCTOR
        self.name = name
        self.role = role
        self.place = place
        pass

    def show_details(self):
        print(f'Hello {self.name} of role {self.role} from {self.place}')

    def show_sumn():
        pass

    def __str__(self) -> str:       # STRING CONSTRUCTOR
        return self.name

person1 = Employee(name='John Doe', role='Data Science Intern', place='Michigan')

print(person1)
# person1.show_details()