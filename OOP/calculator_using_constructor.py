class Calculator:
    # Constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def sum(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 -  self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1 // self.num2
    def mod(self):
        return self.num1 % self.num2

calc = Calculator(20, 10)
print(calc.sum())
print(calc.sub())
print(calc.mul())
print(calc.div())
print(calc.mod())