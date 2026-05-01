# A constructor is a special method that is automatically called when an object is created.
class user:
    def __init__(self,username,email):
        self.username=username
        self.email=email
    
user1=user('krishna24','krishna@gmail.com')
print(user1.email)
print(user1.username)