class User:		# declara una clase y dale el nombre User
    def __init__(self, username, email_address):
        self.name = username			
        self.email = email_address		
        self.account_balance = 0

    # agrega el método deposit 
    def make_deposit(self, amount):
        self.account_balance += amount	# la cuenta del usuario específico aumenta por la cantidad del valor recibido
        return self
    
    def make_withdrawal (self, amount): # toma un argumento que es el monto del débito
        self.account_balance -= amount	# la cuenta del usuario específico disminuye  la cantidad del valor recibido
        return self

    def display_user_balance (self): # imprime el nombre del usuario y el saldo de la cuenta en el terminal
        print('\nUsuario:',self.name,', Saldo:',self.account_balance)
        
    def transfer_money (self, other_user, amount):
        self.account_balance -= amount # Realiza el débito de la cuenta que transfiere
        other_user.make_deposit(amount) # Realiza la acreditación del saldo a la cuenta que recibe
        return self
        
# Se ingresan usuarios
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
alexis = User("Alexis Guamán", "alexis@python.com")

#print(guido.name)	# salida: Guido van Rossum
#print(monty.name)	# salida: Monty Python

# **************  Transacciones realizadas  ************************
# ===> Usuario 1
guido.make_deposit(100).make_deposit(200).make_deposit(50).make_withdrawal(120).transfer_money(alexis,100).display_user_balance()
# ===> Usuario 2
monty.make_deposit(50).make_deposit(150).make_withdrawal(10).make_withdrawal(40).display_user_balance()
# ===> Usuario 3
alexis.make_deposit(500).make_withdrawal(100).make_withdrawal(50).make_withdrawal(90).display_user_balance()


