# A static method does not use object data. It is useful for helper functions.

class mathhelper:
    @staticmethod
    def square(n):
        return n*n
    
print(mathhelper.square(5))