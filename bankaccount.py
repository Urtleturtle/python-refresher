import numpy

class BankAccount:
    def __init__(self,name, accountNumber):
        if(not isinstance(name,str)):
            print("Please enter a valid name")
            return
        
        self.name = name

        self.balance = 0

        if(not isinstance(accountNumber,int)):
            print("Please enter a valid account number")
            return
        
        self.accountNumber = accountNumber

    def withdraw(self,amount):
        if amount > 0:
            try:
                self.balance = self.balance - amount
            except:
                print("Please enter a valid number")
        else:
            print("Please enter a valid number")


    def deposit(self,amount):
        if amount > 0:
            try:
                self.balance = self.balance + amount
            except:
                print("Please enter a valid number")
        else:
            print("Please enter a valid number")

    def printBal(self):
        print(self.balance)