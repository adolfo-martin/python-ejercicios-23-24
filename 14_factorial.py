import os

os.system('cls')


def calcular_factorial(numero):
    resultado = numero
    numero = numero - 1

    while numero >= 1:
        resultado = resultado * numero
        numero = numero - 1

    return resultado


factorial_de_5 = calcular_factorial(5)
print(factorial_de_5)

factorial_de_3 = calcular_factorial(3)
print(factorial_de_3)

numero = int(input("Introduce el número: "))
print(calcular_factorial(numero))