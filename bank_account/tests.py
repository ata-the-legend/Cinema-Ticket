import unittest
import os
from bank_account import AyandehBankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.account = AyandehBankAccount("Alice", 10000)
        self.other_account = AyandehBankAccount("Bob", 20000)

    def test_add(self):
        self.account.add(5000, "password", "cvv2")
        self.assertEqual(self.account._balance, 15000)

    def test_sub(self):
        self.account.sub(5000, "password", "cvv2")
        self.assertEqual(self.account._balance, 5000)

    def test_transfer(self):
        self.account.transfer(self.other_account, 3000, "password", "cvv2")
        self.assertEqual(self.account._balance, 6400)
        self.assertEqual(self.other_account._balance, 23000)

    def test_add_invalid_balance(self):
        with self.assertRaises(ValueError):
            self.account.add(500, "password", "cvv2")

    def test_sub_invalid_balance(self):
        with self.assertRaises(ValueError):
            self.account.sub(9500, "password", "cvv2")

    def test_maximum(self):
        self.assertEqual(AyandehBankAccount.maximum(), 20000)

    def test_save_and_load(self):
        AyandehBankAccount.save()
        AyandehBankAccount.__accounts.clear()
        self.assertEqual(len(AyandehBankAccount.__accounts), 2)
        os.remove("account.pickle")

if __name__ == "__main__":
    unittest.main()