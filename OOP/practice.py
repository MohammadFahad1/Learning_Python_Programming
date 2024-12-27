""" # Multiple Inheritence
class Family:
    def __init__(self, address):
        self.address = address
    
    def __repr__(self) -> str:
        print(f"My Family address is: {self.address}")

class School:
    def __init__(self, id, level):
        self.id = id
        self.level = level

    def __repr__(self) -> str:
        print(f"My School id: {self.id} and level: {self.level}")

class Sports:
    def __init__(self, game):
        self.game = game

    def __repr__(self) -> str:
        print(f"My favourite sports is: {self.game}")

class Student(Family, School, Sports):
    def __init__(address, id, level, game):
        School.__init__(id, level)
        Sports.__init__(game)
        Family.__init__(address)

    def __repr__(self) -> str:
        return f"Address: {self.address}, id: {self.id}, level: {self.level}, game: {self.game}"

fahad = Student("Dhaka", 193015061, "Advanced", "Cricket")
print(fahad) """

""" class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.holder_name = holder_name # public
        self._branch = "Mirpur" # protected
        self.__balance = initial_deposit # private

        # public, private, protected -> these access modifiers

    def deposit(self, amount):
        self.__balance += amount
        return f"You've successfully deposit {amount} taka, your new balance: {self.__balance}"

    def get_balance(self):
        return f"Your current balance is: {self.__balance}"

rafsun = Bank("Chotoo bro", 10000)
print(rafsun.holder_name)
# rafsun.__balance = 0
print(rafsun.deposit(5000))
print(rafsun.get_balance())
print(rafsun._branch)
print(dir(rafsun))
print(rafsun._Bank__balance) """