# Desarrolla una función que conociendo el día y el mes y devuelva la 
# estación del año correspondiente a esa fecha.

import os
os.system('cls')

# día será un número y el mes será un número
def averiguar_estacion(dia, mes):
    if (mes == 12 and dia >= 21) or mes == 1 or mes == 2 or (mes == 3 and dia <21):
        return 'invierno'
    elif (mes == 3 and dia >= 21) or mes == 4 or mes == 5 or (mes == 6 and dia <21):
        return 'primavera'
    elif (mes == 6 and dia >= 21) or mes == 7 or mes == 8 or (mes == 9 and dia <21):
        return 'verano'
    elif (mes == 9 and dia >= 21) or mes == 10 or mes == 11 or (mes == 12 and dia <21):
        return 'otoño'


print(averiguar_estacion(30, 10))
print(averiguar_estacion(19, 3))

dia = int(input('Dame el día: '))
mes = int(input('Dame el mes: '))
print(averiguar_estacion(dia, mes))