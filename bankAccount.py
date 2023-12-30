# This a practice project using instance
# This application consists of functions
# that contains the bank accounts owner's name,
# starting balance which is 0.0, the deposited 
# amount, and the withdraw amount. The deposited
# amount will be added and when the user withdraw
# it will taken out from the balance. Once the
# it was withdrew it will return the current balance.
# it'll also return the owner's name.

class BankAccount:
    def __init__(self,owner):
        self.owner = owner
        self.balance = 0.0
        
    def name(self):
        return f"{self.owner}"
    
    def getBalance(self):
        return self.balance
    
    def withdraw(self,amount):
        print(amount)
        self.balance -= amount
        return f"balance: {self.balance}"
    
    def deposit(self,amount):
        print(self.balance)
        self.balance += amount
        return f"balance: {self.balance}"

acct = BankAccount("Joe", 0.0)

print(acct.name())
print(acct.deposit(20.0))
print(acct.withdraw(15.75))

