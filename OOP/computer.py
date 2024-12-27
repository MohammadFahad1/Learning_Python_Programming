# Inheritance vs Composition

class CPU:
    def __init__(self, cores):
        self.cores = cores
    
    def __repr__(self):
        return f"CPU Cores: {self.cores}"

class RAM:
    def __init__(self, size):
        self.size = size

    def __repr__(self):
        return f"RAM Size: {self.size}"

class HardDrive:
    def __init__(self, capacity):
        self.capacity = capacity

    def __repr__(self):
        return f"Hard Disk Drive: {self.capacity}"

# Computer has a cpu
# Computer has a ram
# Computer has a hard drive
class Computer:
    def __init__(self, cores, size, capacity) -> None:
        self.cpu = CPU(cores)
        self.ram = RAM(size)
        self.hard_disc = HardDrive(capacity)


    def __repr__(self) -> str:
        return f"New Computer with {self.cpu}, {self.ram}, {self.hard_disc}"

mac = Computer(8 ,16, 512)
print(mac)