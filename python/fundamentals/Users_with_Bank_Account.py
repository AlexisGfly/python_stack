class User:		
    def __init__(self, username, email_address):
        self.name = username			
        self.email = email_address		
        # self.account_balance = 0
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        # self.account_balance += amount
        self.account.deposit(amount) 
        # print(self.account.balance)	
        return self
    
    def make_withdrawal (self, amount):
        # self.account_balance -= amount	
        self.account.withdraw(amount) 
        return self

    def display_user_balance (self): 
        # print('\nUsuario:',self.name,', Saldo:',self.account_balance)
        self.account.display_account_info()
        
    def transfer_money (self, other_user, amount):
        # self.account_balance -= amount 
        self.account.deposit(amount) 
        other_user.make_deposit(amount) 
        return self
    
    def interes(self):
        self.account.yield_interest()
        return self

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



# Se ingresan usuarios
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
alexis = User("Alexis Guamán", "alexis@python.com")


# Se realizan las transacciones
guido.make_deposit(500).make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(500).interes().display_user_balance()
alexis.make_deposit(600).make_deposit(250).make_deposit(250).make_withdrawal(100).make_withdrawal(200).make_withdrawal(300).make_withdrawal(400).interes().display_user_balance()



