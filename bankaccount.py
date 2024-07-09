import numpy

class BankAccount:
    def __init__(self,name, initialBalance, accountNumber):
        if(not isinstance(name,str)){
            print("Please enter a valid name")
            break;
        }
        self.name = name

        if(isinstance(initialBalance,float)){
            print("Please enter a valid balance")
            break;
        }
        self.balance = initialBalance

        if(isinstance(accountNumber,int)){
            print("Please enter a valid account number")
            break;
        }
        self.accountNumber = accountNumber

    def withdraw(self,amount):
        try:
            self.balance -= amount
        except:
            print("Please enter a valid number")

    def deposit(self,amount):
        try:
            self.balance += amount
        except:
            print("Please enter a valid number")

    def printBal(self):
        print(self.balance)
        return self.balance