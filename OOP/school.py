class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.id = id
        self.current_class = current_class
    def __repr__(self) -> str:
        return f'Student: {self.name}, class: {self.current_class}, id: {self.id}'
    
class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher: {self.name}, subject: {self.subject}, id: {self.id}'
    
class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.students = []
    
    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        teacher = Teacher(name, subject, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return 'Not enough fee'
        else:
            id = len(self.students) + 1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is enrolled with id: {id}, extra money: {fee - 6500}'
        
    def __repr__(self):
        print('Welcome to ', self.name)
        print('------------- Our Teachers --------------')
        for teacher in self.teachers:
            print(teacher)
        print('------------- Our Students --------------')
        for student in self.students:
            print(student)
        return 'All done for now'

# alia = Student('Alia Torkari', 9, 1)
# ranbeer = Teacher('Douran beer', 'Algorithm', 101)
# print(ranbeer)
# print(alia)

phitron = School("Phitron")
phitron.enroll('Alia', 5200)
phitron.enroll('rani', 8000)
phitron.enroll('aishwariya', 7000)
phitron.enroll('Bhaijan', 9000)

phitron.add_teacher('Tom Cruise', 'Algorithm')
phitron.add_teacher('Decap', 'DS')
phitron.add_teacher('AJ', 'Database')

print(phitron)
