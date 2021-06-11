#Functions Basic II

# 1. Cuenta regresiva : crea una función que acepte un número como entrada. 
# Devuelve una nueva lista que cuenta hacia atrás en uno, desde el número 
# (como el elemento 0) hasta 0 (como el último elemento).
# Ejemplo: la cuenta regresiva (5) debería devolver [5,4,3,2,1,0]

x=5
def cuenta_regresiva(x):
    y=[]
    for i in range(x,0,-1):
        y.append(i)
    return y
print(cuenta_regresiva(x))

# 2. Imprimir y volver : crea una función que recibirá una lista con dos 
# números. Imprima el primer valor y devuelva el segundo.
# Ejemplo: print_and_return ([1,2]) debería imprimir 1 y devolver 2

def print_and_return(a):
    print(a[0])
    return a[1]
print(print_and_return ([1,2]))

# 3. First Plus Length : crea una función que acepta una lista y devuelve la 
# suma del primer valor de la lista más la longitud de la lista.
# Ejemplo: first_plus_length ([1,2,3,4,5]) debería devolver 6 (primer valor: 1 + longitud: 5)

def first_plus_length(a):
    print('primer valor:',a[0])
    print('Longitud:',len(a))
    return(a[0] + len(a))
print(first_plus_length ([1,2,3,4,5]))

# 4. Valores mayores que el segundo : escribe una función que acepte una lista y crea una 
# nueva lista que contenga solo los valores de la lista original que sean mayores que su 
# segundo valor. Imprima cuántos valores son y luego devuelva la nueva lista. Si la lista 
# tiene menos de 2 elementos, haga que la función devuelva False
# Ejemplo: values_greater_than_second ([5,2,3,2,1,4]) debería imprimir 3 y devolver [5,3,4]
# Ejemplo: values_greater_than_second ([3]) debería devolver False

def values_greater_than_second(a):
    greater = []
    if len(a) < 2:
            return(False)
    else:
        for i in range(len(a)):
            if a[1] < a[i]:
                greater.append(a[i])
        
        print(len(greater))
        return(greater)
print(values_greater_than_second ([5,2,3,2,1,4]))
print(values_greater_than_second ([3]))

# 5. Esta longitud, ese valor : escribe una función que acepte dos enteros como parámetros: 
# tamaño y valor. La función debe crear y devolver una lista cuya longitud es igual al 
# tamaño dado y cuyos valores son todos los valores dados.
# Ejemplo: length_and_value (4,7) debería devolver [7,7,7,7]
# Ejemplo: length_and_value (6,2) debería devolver [2,2,2,2,2,2]


def length_and_value(a,b):
    valor=[]
    for i in range(a):
        valor.append(b)
    return (valor)
print(length_and_value(4,7))
print(length_and_value (6,2))