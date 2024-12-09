class Bank:
    balance = 15000
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        print(f"Your current balance is: {self.balance}")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"You've successfully deposit {amount} taka, your new balance: {self.balance}")

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f"Oi Fokir, You can't with below {self.min_withdraw} Taka.")
        elif amount > self.max_withdraw:
            print(f"Bank fokir hoye jabe, You can't with more than {self.max_withdraw}")
        else:
            self.balance -= amount
            print(f"You've successfully withdrawn Tk. {amount}, new balance: {self.balance}")

brac = Bank(15000)

# brac.get_balance()
brac.deposit(1000)
# brac.withdraw(6000)

dbbl = Bank(5000)
dbbl.deposit(5000)
