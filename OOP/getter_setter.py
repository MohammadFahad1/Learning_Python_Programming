# Readonly Property
# Getter Setter
class User:
    def __init__(self, name, age, money):
        self._name = name
        self._age = age
        self.__money = money

    # Getter
    @property
    def age(self):
        return self._age
    
    # Getter
    @property
    def salary(self):
        return self.__money
    
    @salary.setter
    def salary(self, value):
        if value < 0:
            return "Salary cannot be negative!"
        self.__money += value
    
samsu = User('Kopa', 21, 12000)

print(samsu.age)
samsu.salary = 10000
print(samsu.salary)