import os
os.system('cls')

hamburgueserias = ['McDonals', 'Foster\'s Holywood', 'Burguer King', 'Popeye\'s', 'Five Guys']

print(hamburgueserias)
# print(hamburgueserias[2])

# hamburgueserias.remove('Burguer King')
# print(hamburgueserias)

# try:
#     hamburgueserias.remove('Burguer King')
#     print(hamburgueserias)
# except Exception as error:
#     print('Se ha intentado eliminar un elemento que no existe')

hamburgueserias.index

# Inserta un elemento si no existe en la lista
def insertar(lista, elemento):
    try:
        posicion = lista.index(elemento)
    except Exception as error:
        lista.append(elemento)
        return
    
    raise Exception(f'No puedo añadir el elemento {elemento} porque ya está en la lista en la posición {posicion}.')


insertar(hamburgueserias, 'Rohla')
print(hamburgueserias)

try:
    insertar(hamburgueserias, 'Burguer King')
    print(hamburgueserias)
except Exception as error:
    print(error)
