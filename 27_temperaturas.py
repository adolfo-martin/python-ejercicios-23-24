import os
os.system('cls')

temperaturas = [35, 35, 34, 29, 31, 31, 31, 30, 30, 35, 31, 31, 30, 31, 31, 31, 33, 34, 31, 31, 31, 32, 33, 33, 35, 36, 33, 31, 32, 29, 30]


def calcular_temperatura_media(temperaturas):
    suma_total = 0
    for temperatura in temperaturas:
        suma_total += temperatura

    media = suma_total / len(temperaturas)
    return round(media, 1)


def calcular_temperatura_maxima(temperaturas):
    maxima = -100
    for temperatura in temperaturas:
        if temperatura > maxima:
            maxima = temperatura

    return maxima


def calcular_temperatura_minima(temperaturas):
    minima = +100
    for temperatura in temperaturas:
        if temperatura < minima:
            minima = temperatura

    return minima


print(calcular_temperatura_media(temperaturas))
print(calcular_temperatura_maxima(temperaturas))
print(calcular_temperatura_minima(temperaturas))