# En la declaración de la renta se desgrava dinero por cada hijo. 
# Por el primer hijo se desgrava 200 euros, por el segundo hijo se desgrava 250 euros 
# más, y por el tercer o más hijos se desgrava 300 euros más por cada uno de ellos.
# Desarrolla una función que se le diga el número de hijos y calcule el importe 
# total de la desgravación.

# Con un hijo: 200 euros
# Con dos hijos: 450 euros
# Con tres hijos: 750 euros
# Con cuatro hijos: 1050 euros

import os
os.system('cls')

DESGRAVACION_PRIMER_HIJO = 200
DESGRAVACION_SEGUNDO_HIJO = 250
DESGRAVACION_TERCER_HIJO = 300

def calcular_desgravacion(cantidad_hijos):
    if cantidad_hijos <= 0:
        desgravacion = 0
    elif cantidad_hijos == 1:
        desgravacion = DESGRAVACION_PRIMER_HIJO
    elif cantidad_hijos == 2:
        desgravacion = DESGRAVACION_PRIMER_HIJO + DESGRAVACION_SEGUNDO_HIJO
    else:
        desgravacion = DESGRAVACION_PRIMER_HIJO + DESGRAVACION_SEGUNDO_HIJO  \
            + (cantidad_hijos - 2) * DESGRAVACION_TERCER_HIJO
        
    return desgravacion


# print(calcular_desgravacion(1))
# print(calcular_desgravacion(2))
# print(calcular_desgravacion(3))
# print(calcular_desgravacion(4))

cantidad_hijos = int(input('Cuántos hijos tienes: '))
desgravacion = calcular_desgravacion(cantidad_hijos)
print(f'La desgrabación que corresponde a {cantidad_hijos} hijos es {desgravacion} euros.')