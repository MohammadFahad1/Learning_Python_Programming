# Base class, parent class, common attribute + functionality class
class Gadget:
    def __init__(self, brand, price, color, origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin
    
    def run(self):
        return f'Running gadget: {self.brand}'

# Derived class, child class, uncommon attribute + functionality class
class Laptop:
    def __init__(self, memory, ssd):
        self.memory = memory
        self.ssd = ssd

    def run(self):
        return f'Running Laptop: {self.brand}'
    
    def coding(self):
        return f'Learning python and practicing'
    
class Phone(Gadget):
    def __init__(self, dual_sim):
        self.dual_sim = dual_sim

    def run(self):
        return f'Phone tipa tipi kore'

    def phone_call(self, number, text):
        return f'Sending SMS to {number} with {text}'
    
    def __repr__(self):
        return f'Phone: {self.dual_sim}'
    
class Camera:
    def __init__(self, pixel):
        self.pixel = pixel

    def run(self):
        pass

    def change_lens(self):
        pass

# inheritance
my_phone = Phone(True)
# my_phone.dual_sim()
# my_phone.phone_call()
my_phone.brand
print(my_phone)