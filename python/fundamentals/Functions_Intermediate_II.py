# 1. Actualiza los valores en diccionarios y listas 
# Cambia el valor 10 en x a 15. Una vez que haya terminado, x ahora debería ser [[5,2,3], [15,8,9]].
# Cambia el apellido del primer alumno de 'Jordan' a 'Bryant'
# En el directorio sports_directory, cambia 'Messi' a 'Andres'
# Camba el valor 20 en z a 30
print('\n***********    Ejercicio 1    ***********\n')

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def actualiza():
    x[1][0] = 15
    students[0]['last_name'] = 'Bryan'
    sports_directory['soccer'][0] = 'Andres'
    z[0]['y'] = 30



actualiza()
print('\nActividad 1: x ahora es ',x)
print('Actividad 2: El apellido de Michael ahora es',students[0]['last_name'])
print('Actividad 3: Deportes Soccer ahora es',sports_directory['soccer'])
print('Actividad 4: z ahora es ',z)



# 2. Itera a través de una lista de diccionarios
# Crea una función iterateDictionary(some_list) que, dada una lista de diccionarios, 
# la función recorra cada diccionario de la lista e imprime cada clave y el valor asociado. Por ejemplo, dada la siguiente lista:

print('\n***********    Ejercicio 2    ***********\n')

def iterateDictionary(some_list):
    for i in range(len(students)):
        print('first_name -',students[i]['first_name'],',last_name -',students[i]['last_name'])

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 




# 3. Obtén valores de una lista de diccionarios
# Crea una función iterateDictionary2(key_name, some_list)que, dada una lista 
# de diccionarios y un nombre de clave, la función imprima el valor almacenado 
# en esa clave para cada diccionario.
print('\n***********    Ejercicio 3    ***********\n')

def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])


iterateDictionary2 ('first_name', students)
print('\n')
iterateDictionary2('last_name', students)



# 4.Itera a través de un diccionario con valores de listas
# Crea una función printInfo(some_dict) que, dado un diccionario cuyos valores 
# son todas listas, imprima el nombre de cada clave junto con el tamaño de su 
# lista, y luego imprima los valores asociados dentro de la lista de cada clave. 

print('\n***********    Ejercicio 4    ***********\n')

def printInfo(some_dict):
    claves = list(some_dict.keys())
    for i in range(len(claves)):
        print(len(some_dict[claves[i]]), (claves[i]).upper())
        for j in range(len(some_dict[claves[0]])):
            print(some_dict[claves[i]][j])


dojo = {'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
        'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
        }
printInfo(dojo)
