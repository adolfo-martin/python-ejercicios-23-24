import os
os.system('cls')

NOMBRE = 0
GENERO = 1
ALTURA = 2
MASA = 3

clientes_gimnasio = [
    ['Juan', 'M', 182, 92],
    ['Alicia', 'F', 157, 52],
    ['Manuel', 'M', 171, 75],
    ['Sonia', 'F', 152, 51],
    ['Jimena', 'F', 165, 64],
    ['Carlos', 'M', 169, 67],
    ['Sara', 'F', 163, 54],
    ['Ramiro', 'M', 192, 89],
    ['Josefina', 'F', 164, 58]
]

def devolver_nombre_persona_mas_alta(personas):
    altura_maxima = 0
    nombre_maximo = ''

    for persona in personas:
        if persona[ALTURA] > altura_maxima:
            altura_maxima = persona[ALTURA]
            nombre_maximo = persona[NOMBRE]
    
    return nombre_maximo

print(devolver_nombre_persona_mas_alta(clientes_gimnasio))


def calcular_masa_corporal(masa_kilogramos, estatura_metros):
    return masa_kilogramos / estatura_metros**2