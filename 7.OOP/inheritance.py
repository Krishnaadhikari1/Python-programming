# Inheritance means one class can use the properties and methods of another class. It helps reuse code.
class user:
    def __init__(self,name):
        self.name = name
    
    def login(self):
        print(self.name,"logged in")
class student(user):
    def study(self):
        print(self.name," is studing .")

s1=student("krishna")
s1.login()
s1.study()