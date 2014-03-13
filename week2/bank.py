class BankAccount():
    """Docstring for our BankAccount"""
    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount < 0:
            return False

        self.__balance += amount

        return True

    def withdraw(self, amount):
        if self.__balance - amount < 0:
            return False

        self.__balance -= amount
        return True
