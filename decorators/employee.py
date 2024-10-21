class Employee:

    # ATTRIBUTES
    name : str
    role : str
    salary = int
    place : str

    def details(self, name,role, salary, place):
        self.name = name
        self.role = role
        self.salary = salary
        self.place = place

    @property       # @property decorator is a built-in decorator that allows you to define methods in a class that can be accessed like attributes. This provides a way to implement getter and setter methods while keeping the syntax clean and intuitive.
    def show_name(self):
        return self.name
    
    def show_place(self):
        return self.place
    
person1 = Employee()

person1.details(name='John Doe', role='Trainee', salary=123, place='Ernakulam')

print(person1.show_name)
print(person1.show_place())