# Encapsulation means keeping data and methods together inside a class. It also helps protect data.
class bankaccount:
    def __init__(self,balance):
        self.__balance = balance  #private variable

    def deposit(self,amount):
        self.__balance += amount

    def show_balance(self):
        print("Balance :",self.__balance)

account = bankaccount(5000)
account.deposit(2000)
account.show_balance()