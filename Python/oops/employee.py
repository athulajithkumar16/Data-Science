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

    def show_detail(self):
        print(f'Hello {self.name} from {self.place}')

    def method3(self):
        print(f'{self.name} with salary {self.salary}')
        # print(type(self.salary))

person1 = Employee()

person1.details(name='John Doe', role='Trainee', salary=123, place='Ernakulam')
person1.show_detail()
person1.method3()