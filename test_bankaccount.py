import unittest
import bankaccount


class TestBankAccount(unittest.TestCase):
    def test_bankaccount(self):
        myAccount = bankaccount.BankAccount("bruh",543,3848)
        self.assertEqual(myAccount.name, "bruh")
        self.assertEqual(myAccount.balance, 543)
        self.assertEqual(myAccount.accountNumber, 3848)

if __name__ == "__main__":
    unittest.main()
