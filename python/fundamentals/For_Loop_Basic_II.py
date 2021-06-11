# For Loop Basic II

# 1. Tamaño grande: dada una lista, escriba una función que cambie 
# todos los números positivos de la lista a "big".
# Ejemplo: biggie_size ([- 1, 3, 5, -5]) devuelve la misma lista, 
# pero cuyos valores son ahora [-1, "big", "big", -5]

def biggie_size(a):
    for i in range(len(a)):
        if a[i] > 0:
            a[i]="big"
    return(a)

print(biggie_size ([- 1, 3, 5, -5]))

# 2. Contar positivos : dada una lista de números, cree una función 
# para reemplazar el último valor con el número de valores positivos. 
# (Tenga en cuenta que cero no se considera un número positivo).
# Ejemplo: count_positives([- 1, 1, 1,1 ]) cambia la lista original 
# a [-1, 1, 1, 3] y la devuelve
# Ejemplo: count_positives([1, 6, -4, -2, -7, -2]) cambia la lista 
# a [1, 6, -4, -2, -7, 2] y la devuelve

def count_positives(a):
    num_pos=0
    for i in range(len(a)):
        if a[i] > 0:
            num_pos = num_pos+1
    a[-1] = num_pos
    return(a)
print(count_positives([- 1, 1, 1,1 ]))
print(count_positives([1, 6, -4, -2, -7, -2]))

# 3. Suma total : crea una función que toma una lista y devuelve la 
# suma de todos los valores de la matriz.
# Ejemplo: sum_total ([1,2,3,4]) debería devolver 10
# Ejemplo: sum_total ([6,3, -2]) debería devolver 7

def sum_total(a):
    sum=0
    for i in range(len(a)):
        sum = sum + a[i]
    return(sum)
print(sum_total ([1,2,3,4]))
print(sum_total ([6,3, -2]))

# 4. Promedio : crea una función que toma una lista y devuelve el 
# promedio de todos los valores.
# Ejemplo: el promedio ([1,2,3,4]) debería devolver 2.5

def promedio(a):
    sum=0
    for i in range(len(a)):
        sum = sum + a[i]
    return(sum / len(a))
print(promedio ([1,2,3,4]))

# 5. Longitud : crea una función que toma una lista y devuelve la 
# longitud de la lista.
# Ejemplo: la longitud ([37,2,1, -9]) debería devolver 4
# Ejemplo: longitud ([]) debería devolver 0

def longitud(a):
    return(len(a))
print(longitud ([37,2,1, -9]))
print(longitud ([]))

# 6. Mínimo : crea una función que tome una lista de números y 
# devuelva el valor mínimo en la lista. Si la lista está vacía, 
# haga que la función devuelva False.
# Ejemplo: mínimo ([37,2,1, -9]) debería devolver -9
# Ejemplo: mínimo ([]) debería devolver False

def minimo(a):
    if len(a) == 0:
        return(False)
    else:
        min = a[0]
        for i in range(len(a)):
            if min > a[i]:
                min = a[i]
        return(min)
print(minimo ([37,2,1, -9]))
print(minimo ([]))

# 7. Máximo : crea una función que toma una lista y devuelve el 
# valor máximo en la matriz. Si la lista está vacía, haga que la 
# función devuelva False.
# Ejemplo: máximo ([37,2,1, -9]) debería devolver 37
# Ejemplo: máximo ([]) debería devolver False

def maximo(a):
    if len(a) == 0:
        return(False)
    else:
        max = a[0]
        for i in range(len(a)):
            if max < a[i]:
                max = a[i]
        return(max)
print(maximo ([37,2,1, -9]))
print(maximo ([]))

# 8. Análisis final : crea una función que tome una lista y devuelva 
# un diccionario que tenga la suma total, promedio, mínimo, máximo 
# y longitud de la lista.
# Ejemplo: ultimate_analysis ([37,2,1, -9]) debería devolver 
# {'total': 31, 'promedio': 7.75, 'minimo': -9, 'maximo': 37, 'longitud': 4}

def ultimate_analysis(a):
    sum = 0
    max = min = a[0]
    for i in range(len(a)):
        sum = sum + a[i]
        if max < a[i]:
                max = a[i]
        if min > a[i]:
                min = a[i]
    prom = sum / len(a)
    return({'total':sum,'promedio':prom,'minimo':min,'maximo':max,'longitud':len(a)})
print(ultimate_analysis ([37,2,1, -9]))

# 9. Lista inversa : crea una función que tome una lista y la devuelva con
# los valores invertidos. Haz esto sin crear una segunda lista. 
# (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).
# Ejemplo: reverse_list ([37,2,1, -9]) debería devolver [-9,1,2,37]

def reverse_list(a):
    return(a[::-1])
print(reverse_list ([37,2,1, -9]))







