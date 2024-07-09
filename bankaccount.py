import numpy

class BankAccount:
    def __init__(self,name, accountNumber):
        if(not isinstance(name,str)):
            raise Exception("Please enter a valid name")
            return
        
        self.name = name

        self.balance = 0

        if(not isinstance(accountNumber,int)):
            raise Exception("Please enter a valid account number")
            return
        
        self.accountNumber = accountNumber

    def withdraw(self,amount):
        if amount <= 0: 
            raise Exception("Error: Please enter a valid number")
        if amount > self.balance:
            raise Exception("Error: Insufficient balance")

        try:
            self.balance = self.balance - amount
        except:
            raise Exception("Error: Please enter a valid number")

    def deposit(self,amount):
        if amount <= 0: 
            raise Exception("Error: Please enter a valid number")

        try:
            self.balance = self.balance + amount
        except:
            raise Exception("Error: Please enter a valid number")

    def printBal(self):
        print(self.balance)