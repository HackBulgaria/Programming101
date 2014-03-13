import bank
import unittest


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.bank_account = bank.BankAccount()

    """Tests for BankAccount class"""
    def test_init_bank_account_object(self):
        self.assertEqual(0, self.bank_account.get_balance())

    def test_deposit_money(self):
        result = self.bank_account.deposit(100)

        self.assertTrue(result)
        self.assertEqual(100, self.bank_account.get_balance())

    def test_deposit_negative_amount_of_money(self):
        result = self.bank_account.deposit(-100)

        self.assertTrue(not result)
        self.assertEqual(0, self.bank_account.get_balance())

    def test_withdraw_from_deposited_bank_account(self):
        self.bank_account.deposit(100)

        result = self.bank_account.withdraw(50)

        self.assertTrue(result)
        self.assertEqual(50, self.bank_account.get_balance())

    def test_withdraw_from_bank_account_with_insufficient_funds(self):
        result = self.bank_account.withdraw(1000)

        self.assertTrue(not result)
        self.assertEqual(0, self.bank_account.get_balance())

if __name__ == '__main__':
    unittest.main()
