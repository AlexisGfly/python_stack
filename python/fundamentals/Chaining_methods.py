class User:		# declara una clase y dale el nombre User
    def __init__(self, username, email_address):
        self.name = username			
        self.email = email_address		
        self.account_balance = 0

    # agrega el método deposit 
    def make_deposit(self, amount):	# toma un argumento que es el monto del depósito
    	 self.account_balance += amount	# la cuenta del usuario específico aumenta por la cantidad del valor recibido
    
    def make_withdrawal (self, amount): # toma un argumento que es el monto del débito
        self.account_balance -= amount	# la cuenta del usuario específico disminuye  la cantidad del valor recibido

    def display_user_balance (self): # imprime el nombre del usuario y el saldo de la cuenta en el terminal
        print('\nUsuario:',self.name,', Saldo:',self.account_balance)
        
    def transfer_money (self, other_user, amount):
        self.account_balance -= amount # Realiza el débito de la cuenta que transfiere
        other_user.make_deposit(amount) # Realiza la acreditación del saldo a la cuenta que recibe
        
# Se ingresan usuarios
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
alexis = User("Alexis Guamán", "alexis@python.com")

#print(guido.name)	# salida: Guido van Rossum
#print(monty.name)	# salida: Monty Python

# **************  Transacciones realizadas  ************************
# ===> Usuario 1
# Depósitos
guido.make_deposit(100) # Depósito 1
guido.make_deposit(200) # Depósito 2
guido.make_deposit(50)  # Depósito 2
# Retiros
guido.make_withdrawal(120) # Retiro 1
# Muestra saldo
guido.display_user_balance() # Saldo actual


# ===> Usuario 2
# Depósitos
monty.make_deposit(50)  # Depósito 1
monty.make_deposit(150) # Depósito 2
# Retiros
monty.make_withdrawal(10) # Retiro 1
monty.make_withdrawal(40) # Retiro 2
# Muestra saldo
monty.display_user_balance()


# ===> Usuario 3
# Depósitos
alexis.make_deposit(500)  # Depósito 1
# Retiros
alexis.make_withdrawal(100) # Retiro 1
alexis.make_withdrawal(50)  # Retiro 2
alexis.make_withdrawal(90)  # Retiro 3
# Muestra saldo
alexis.display_user_balance()

# ===> Transferencias del Usuario 1 al Usuario 3
# Transferencia realizada
guido.transfer_money(alexis,100)
# Imprime saldos
print('\nSaldo posterior a la transferencia interbancaria')
guido.display_user_balance()
alexis.display_user_balance()