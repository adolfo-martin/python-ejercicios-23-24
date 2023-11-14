import os
import random

os.system('clear')

def generar_numeros_aleatorios(cantidad, limite_inferior, limite_superior):
    numeros = []
    for i in range(0, cantidad):
        numero = random.randint(limite_inferior, limite_superior)
        numeros.append(numero)

    return numeros


def filtrar_pares(numeros):
    pares = []
    for numero in numeros:
        if es_par(numero):
            pares.append(numero)

    return pares


def filtrar_impares(numeros):
    impares = []
    for numero in numeros:
        if not es_par(numero):
            impares.append(numero)

    return impares


def es_par(numero):
    if numero % 2 == 0:
        return True
    else: 
        return False
    

numeros = generar_numeros_aleatorios(1000, 1000, 3000)
print(numeros[0:10])

pares = filtrar_pares(numeros)
print(pares[0:10])

impares = filtrar_impares(numeros)
print(impares[0:10])