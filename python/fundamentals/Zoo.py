class Animal:
    def __init__(self, nombre, edad, n_salud, n_felicidad):
        self.nombre = nombre
        self.edad = edad
        self.n_salud = n_salud
        self.n_felicidad = n_felicidad
        
    def display_info(self):
        print('*'*20,'\nTipo de animal:',self.tipo,'\nNombre:',self.nombre,'\nSalud:',self.n_salud,'\nFelicidad:',self.n_felicidad)
        
    def alimentacion(self,comida):
        self.n_salud += comida
        self.n_felicidad += comida
        
class Leon(Animal):
    def __init__(self, nombre, edad, n_salud, n_felicidad, tipo):
        super().__init__(nombre, edad, n_salud, n_felicidad)
        self.tipo = tipo 
    def alimentacion(self,tipo_comida):
        self.tipo_comida = tipo_comida
        
        if self.tipo_comida == 'carne':
            super().alimentacion(30)
        if self.tipo_comida == 'pollo':
            super().alimentacion(15)
        if self.tipo_comida == 'fruta':
            super().alimentacion(10)

class Tigre(Animal):
    def __init__(self, nombre, edad, n_salud, n_felicidad, tipo):
        super().__init__(nombre, edad, n_salud, n_felicidad)
        self.tipo = tipo 
    def alimentacion(self,tipo_comida):
        self.tipo_comida = tipo_comida
        
        if self.tipo_comida == 'carne':
            super().alimentacion(40)
        if self.tipo_comida == 'pollo':
            super().alimentacion(20)
        if self.tipo_comida == 'fruta':
            super().alimentacion(20)

class Oso(Animal):
    def __init__(self, nombre, edad, n_salud, n_felicidad, tipo):
        super().__init__(nombre, edad, n_salud, n_felicidad)
        self.tipo = tipo 
    def alimentacion(self,tipo_comida):
        self.tipo_comida = tipo_comida
        
        if self.tipo_comida == 'carne':
            super().alimentacion(20)
        if self.tipo_comida == 'pollo':
            super().alimentacion(10)
        if self.tipo_comida == 'fruta':
            super().alimentacion(40)

        

# print('\n')
# # Se define el animal
# simba = Leon('Simba', 3, 70, 70,'León')
# # Acciones a realizar
# simba.alimentacion('fruta')
# simba.display_info()

# print('\n')
# # Se define el animal
# simba = Tigre('Rajah', 4, 50, 40,'Tigre')
# # Acciones a realizar
# simba.alimentacion('fruta')
# simba.display_info()

# print('\n')
# # Se define el animal
# simba = Oso('Yogi', 5, 70, 80,'Oso')
# # Acciones a realizar
# simba.alimentacion('fruta')
# simba.display_info()        
    
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name
        
    def add_lion(self, nombre, edad, n_salud, n_felicidad, tipo):
        self.animals.append( Leon (nombre, edad, n_salud, n_felicidad, tipo) )
        
    def add_tiger(self, nombre, edad, n_salud, n_felicidad, tipo):
        self.animals.append( Tigre (nombre, edad, n_salud, n_felicidad, tipo) )
        
    def add_bear(self, nombre, edad, n_salud, n_felicidad, tipo):
        self.animals.append( Oso (nombre, edad, n_salud, n_felicidad, tipo) )
        
    def print_all_info(self):
        print("-"*30, self.name, "-"*30)
        for animal in self.animals:
            animal.display_info()
            
zoo1 = Zoo("Alexis's Zoo")

zoo1.add_lion('Nala', 3, 70, 70,'León')
zoo1.add_lion('Simba', 2, 60, 50,'León')

zoo1.add_tiger('Rajah', 4, 50, 40,'Tigre')
zoo1.add_tiger('Shere Khan', 3, 60, 40,'Tigre')

zoo1.add_bear('Yogi', 5, 70, 80,'Oso')

zoo1.print_all_info()