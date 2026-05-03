# Methods are functions inside a class. Instance methods usually use self
class calculator:
    def add(self,a,b):
        return a+b
    
calc=calculator()
print(calc.add(10,6))
 