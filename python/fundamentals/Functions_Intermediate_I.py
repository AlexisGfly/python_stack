import random

def randInt(min=0,max=100):
    if min < max and max > 0:
        num = (random.randint(min,max))
    else:
        return(False)
    return (num)

print(randInt())
print(randInt(max=50)) 
print(randInt(min=50))
print(randInt(min=50, max=500)) 


# Bonus Juega al Loto

def loto(num='',su_boleto=''):
    # Se define número de lotería como lista vacía
    loteria = []
    # Se genera una lista de 4 números aleatorios
    for i in range(4):
        loteria.append(random.randint(0,num))
    # Se realiza comparativa con el boleto del participante
    if loteria == su_boleto:
        resultado = 'Felicidades...! usted es el ganador'
    else:
        resultado = 'Siga participando'
    return(loteria, resultado)

su_boleto=[1,2,3,4]
num=10    
salida = loto(num,su_boleto)

print('*******************************************************************')
print('\t====> Juego de la Lotería <====\n\t Su boleto es: ',su_boleto,'\n')
print('\tEl valor ganador es:',salida[0],'====>',salida[1],'\t')
print('*******************************************************************')

