# A child class can change the behavior of a parent class method.
class user:
    def role(self):
        print("normal user ")

class admin(user):
    def role(self):
        print("admin user")

u1=user()
a1=admin()

u1.role()
a1.role()