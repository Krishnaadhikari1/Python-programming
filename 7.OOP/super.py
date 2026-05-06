# super() is used to call the parent class constructor or method.

class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll

s1 = Student("Krishna", 101)

print(s1.name)
print(s1.roll)