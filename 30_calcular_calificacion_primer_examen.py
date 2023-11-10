import os
os.system('cls')

ponderaciones = [0.75, 0.75, 1.00, 1.00, 1.25, 1.50, 2.00, 1.75]


def calcular_calificacion(ponderaciones, calificaciones):
    calificacion = 0
    for i in range(0, len(ponderaciones)):
        calificacion += ponderaciones[i] * calificaciones[i]

    calificacion /= 100
    return calificacion


def pedir_calificaciones():
    calificaciones = []
    cuantas = int(input('Cuántas preguntas tiene el examen: '))

    for i in range(1, cuantas+1):
        calificacion = int(input(f'Dime la calificación de la pregunta {i}: '))
        calificaciones.append(calificacion)

    return calificaciones


# print(calcular_calificacion(ponderaciones, [5, 5, 5, 5, 5, 5, 5, 5]))
# print(calcular_calificacion(ponderaciones, [0, 0, 0, 0, 0, 0, 0, 0]))
# print(calcular_calificacion(ponderaciones, [10, 10, 10, 10, 10, 10, 10, 10]))

calificaciones = pedir_calificaciones()
print(calcular_calificacion(ponderaciones, calificaciones))
