from week04.tasks import classes

def test_greet():
    person = classes.Person("Gacek", 25)
    assert person.greet() == "Hello, my name is Gacek"

def test_deposit():
    account = classes.BankAccount()
    account.deposit(100)
    assert account.balance == 100

def test_withdraw():
    account = classes.BankAccount()
    account.deposit(100)
    account.withdraw(40)
    assert account.balance == 60
