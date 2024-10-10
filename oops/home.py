# Create a class for bank with attributes 
# attributes : name, place, account_type, balance, bank_name
# methods : show_details, deposit, withdrawal, balance

class Bank:

    bank_name = 'SBI Bank'
    balance : int

    def __init__(self, name, place, account_type, balance):
        self.name = name
        self.place = place
        self.account_type = account_type
        self.balance = int(balance)

    def __str__(self) -> str:
        return self.name
    
    def show_details(self):
        print(f'Name : {self.name} \nPlace : {self.place} \nAccount Type : {self.account_type} \nBalance : {self.balance} \nBank : {self.bank_name}')

    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance + self.amount
        print(f'Balance after deposit : {self.balance}')

    def withdrawal(self, amount):
        self.amount = amount
        if self.amount < self.balance:
            self.balance = self.balance - self.amount
            print(f'Balance after withdrawal : {self.balance}')
        else:
            print('Error ! Withdraw amount greater than balance')

    def show_balance(self):
        print(f'Balance: {self.balance}')

person1 = Bank('John Doe', 'Scranton', 2132, 2000)      # OBJECT

# print(person1)
person1.show_details()
person1.deposit(5000)
person1.withdrawal(1700)
person1.show_balance()