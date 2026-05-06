# Class variables are shared by all objects of the class.

class student:
    college = "tribhuvan university "
    def __init__(self,name):
        self.name = name 

s1= student("dhiran")
s2=student("kiran")

print(s1.college)
print(s2.college)