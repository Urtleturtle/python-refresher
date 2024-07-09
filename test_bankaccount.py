import unittest
import bankaccount


class TestBankAccount(unittest.TestCase):
    def test_bank_init(self):
        myAccount = bankaccount.BankAccount("bruh", 3848)
        self.assertEqual(myAccount.name, "bruh")
        self.assertNotEqual(myAccount.name, "lol")

        self.assertEqual(myAccount.balance, 0)
        self.assertNotEqual(myAccount.balance, 500)

        self.assertEqual(myAccount.accountNumber, 3848)
        self.assertNotEqual(myAccount.accountNumber, 3844)

    def test_bank_deposit(self):
        myAccount = bankaccount.BankAccount("bruh", 3848)
        myAccount.deposit(50)
        self.assertEqual(myAccount.balance, 50)
        self.assertNotEqual(myAccount.balance, 1)

        myAccount.deposit(-50)
        self.assertEqual(myAccount.balance, 50)
        self.assertNotEqual(myAccount.balance, 0)

    def test_bank_withdraw(self):
        myAccount = bankaccount.BankAccount("bruh", 3848)
        self.balance = 100
        myAccount.withdraw(50)
        self.assertEqual(myAccount.balance, 50)
        self.assertNotEqual(myAccount.balance, 150)

        myAccount.withdraw(-100)
        self.assertEqual(myAccount.balance, 50)
        self.assertNotEqual(myAccount.balance, 150)

        myAccount.withdraw(5000)
        self.assertEqual(myAccount.balance, 50)
        self.assertNotEqual(myAccount.balance, 0)

if __name__ == "__main__":
    unittest.main()
