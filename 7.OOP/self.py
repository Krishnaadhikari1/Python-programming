# self refers to the current object. It is used to access variables and methods inside the class.
class student:
    def __init__(self,name):
        self.name=name

    def show_name(self):
        print("student name :", self.name)

s1=student("krishna ")
s1.show_name()