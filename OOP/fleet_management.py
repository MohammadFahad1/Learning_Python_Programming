# Ena Poribohon
class Company:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.bus = []
        self.routes = []
        self.drivers = []
        self.manager = []
        self.supervisors = []
        self.fare = []

class Driver:
    def __init__(self, name, license, age):
        self.name =  name
        self.license = license
        self.age = age

class Counter:
    def __init__(self):
        pass

    def purchase_a_ticket(self, start, destination):
        pass

class Passenger:
    pass

class Supervisors:
    pass

red_mia = Driver('Fahad', 123, 25)