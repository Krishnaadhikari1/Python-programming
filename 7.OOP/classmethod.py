# A class method works with the class itself, not a single object.

class User:
    total_users = 0
    
    def __init__(self, name):
        self.name = name
        User.total_users += 1

    @classmethod
    def show_total_users(cls):
        print("Total users:", cls.total_users)

u1 = User("Krishna")
u2 = User("Ram")

User.show_total_users()