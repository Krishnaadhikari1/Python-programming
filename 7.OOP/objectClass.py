'''A class is a blueprint.
   An object is a real item created from that class.
   Example: Student is a class, and student1 is an object.  '''

class student:
    def __init__(self,name, mark):
        self.name=name
        self.mark=mark

student1= student("krishna",99)

print(student1.mark)