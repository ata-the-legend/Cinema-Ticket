import unittest
from bank_account import BankAccount

class TestBankAccount(unittest.TestCase):

    def test_create_account(self):
        account = BankAccount.create_account('Pouriya', 'Blu', 500_000_000)
        self.assertEqual(account.owner_name, 'Pouriya')
        self.assertEqual(account.bank, 'Blu')
        self.assertIsInstance(account.serial_number, str)
        self.assertEqual(len(account.serial_number), 19)
        self.assertIsInstance(account.cvv2, str)
        self.assertEqual(len(account.cvv2), 3)
        self.assertIsInstance(account._BankAccount__password, str)
        self.assertEqual(len(account._BankAccount__password), 4)
        self.assertEqual(account._BankAccount__balance, 500_000_000)

    def test_add(self):
        account = BankAccount.create_account('Pouriya','Blu', 500_000_000)
        balance = account.add(55_555_555)
        self.assertEqual(balance, 555_555_555)

    def test_sub(self):
        account = BankAccount.create_account('Pouriya', 'Blu', 500_000_000)
        balance = account.sub(100_000_000, account._BankAccount__password)
        self.assertEqual(balance, 400_000_000)

    def test_transfer_to_another(self):
        account1 = BankAccount.create_account('Pouriya', 'Blu', 500_000_000)
        account2 = BankAccount.create_account('Ali Karimi', 'Blu', 800_000_000)
        account1.transfer_to_another(account2, 88_888_888, account1._BankAccount__password, account1.cvv2)
        self.assertEqual(account1._BankAccount__balance, 411_110_112)
        self.assertEqual(account2._BankAccount__balance, 888_888_888)

    def test_is_serial(self):
        account = BankAccount.create_account('Ali Aghaa Karimi', 'Blu', 888_888_888)
        self.assertTrue(BankAccount.is_serial(account.serial_number))
        self.assertFalse(BankAccount.is_serial('invalid_serial_number'))

if __name__ == '__main__':
    unittest.main()