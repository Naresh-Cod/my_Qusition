
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
name = input("Enter your name: ")
age = input("Enter your age:")

sos = Student(name, age)
print(sos.name)
print(sos.age)
