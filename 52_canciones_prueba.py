PONDERACIONES = [0.5, 0.5, 1, 1.5, 2, 1.5, 3]
calificaciones = [10, 10, 10, 10, 10, 10, 5]

def calcular_calificacion(calificaciones):
    suma = 0
    for i in range(0, len(PONDERACIONES)):
        suma = suma + PONDERACIONES[i] * calificaciones[i]

    calificacion = suma / 10
    return calificacion


print(calcular_calificacion(calificaciones))



# canciones = [
#     { 'interprete': 'Daddy Yankee', 'titulo': 'La gasolina', 'valoracion': 1 },
#     { 'interprete': 'U2', 'titulo': 'With or without you', 'valoracion': 9 },
#     { 'interprete': 'Queen', 'titulo': 'Bohemian Rapsody', 'valoracion': 10 },
#     { 'interprete': 'Raw Alejandro', 'titulo': 'sdafqawrewr', 'valoracion': 0},
#     { 'interprete': 'The Beatles', 'titulo': 'Yellow Submarine', 'valoracion': 7},
# ]


# def ordenar_por_valoracion(canciones):

#     for i in range(0, len(canciones)-1):
#         maximo = -1
#         posicion_maximo = -1

#         for j in range(i, len(canciones)):
#             if canciones[j]['valoracion'] > maximo:
#                 maximo = canciones[j]['valoracion']
#                 posicion_maximo = j
        
#         cancion_auxiliar = canciones[i]
#         canciones[i] = canciones[posicion_maximo] 
#         canciones[posicion_maximo] = cancion_auxiliar
        
#     return canciones


# canciones_ordenadas = ordenar_por_valoracion(canciones)
# print(canciones_ordenadas)