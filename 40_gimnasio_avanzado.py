import os
# from operator import itemgetter

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


print(calcular_masa_corporal(68, 165/100))

def mostrar_masas_corporales(clientes):
    print('Las masas corporales son:')

    for cliente in clientes:
        masa_corporal = calcular_masa_corporal(cliente[MASA], cliente[ALTURA] / 100)
        print(f'La masa corporal de {cliente[NOMBRE]} es {masa_corporal}')


os.system('cls')
# mostrar_masas_corporales(clientes_gimnasio)

def mostrar_masas_corporales_ordenadas(clientes):
    masas_corporales = []

    for cliente in clientes:
        masa_corporal = calcular_masa_corporal(cliente[MASA], cliente[ALTURA] / 100)
        masas_corporales.append( [masa_corporal, cliente[NOMBRE]] )

    masas_corporales.sort()
    print('Las masas corporales son:')
    for cliente in masas_corporales:
        print(f'La masa corporal de {cliente[1]} es {cliente[0]:0.2f}')


mostrar_masas_corporales_ordenadas(clientes_gimnasio)