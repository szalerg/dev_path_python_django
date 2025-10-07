#Prosta klasa
#Stwórz klasę Person, która ma atrybuty name i age, oraz metodę greet(), która zwraca "Hello, my name is <name>".
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Person: {self.name}"
    def greet(self):
        return f"Hello, my name is {self.name}"

#Klasa BankAccount
#Stwórz klasę BankAccount z metodami deposit(amount), withdraw(amount) i get_balance(). Saldo początkowe to 0, nie można wypłacić więcej niż jest na koncie

class BankAccount:

    def __init__(self):
        self.balance = 0
        
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            return "Brak środków"