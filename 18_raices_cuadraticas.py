# Averigua que son las raíces de una función cuadrática.
# Desarrolla dos funciones que nos devuelvan cada una de las raíces. 

import math

def calcular_raiz_suma(a, b, c):
    raiz = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    return raiz


def calcular_raiz_resta(a, b, c):
    raiz = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    return raiz


# print(calcular_raiz_suma(1, -5, 6))
# print(calcular_raiz_resta(1, -5, 6))

a = int(input("Dime el valor de a: "))
b = int(input("Dime el valor de b: "))
c = int(input("Dime el valor de c: "))

raiz1 = calcular_raiz_suma(a, b, c)
raiz2 = calcular_raiz_resta(a, b, c)

print(f"Las raices para ({a}, {b}, {c}) son ({raiz1}, {raiz2})")