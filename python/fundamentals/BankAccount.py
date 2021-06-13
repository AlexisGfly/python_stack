class BankAccount:
    def __init__(self, int_rate, balance):
        self.rate = int_rate
        self.account_balance = balance

    def deposit(self, amount):
        self.account_balance += amount
        return self
    def withdraw(self, amount):
        self.account_balance -= amount
        return self
    def display_account_info(self):
        print('\tSaldo:',self.account_balance)

    def yield_interest(self):
        if self.account_balance > 0:
            self.account_balance = self.account_balance * self.rate + self.account_balance
            return self

guido = BankAccount(0.01, 500)
alexis = BankAccount(0.01, 600)

guido.deposit(100).deposit(200).deposit(300).withdraw(500).yield_interest().display_account_info()
alexis.deposit(250).deposit(250).withdraw(100).withdraw(200).withdraw(300).withdraw(400).yield_interest().display_account_info()
