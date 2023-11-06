import os
os.system('cls')

lenguajes = ['Java', 'Python', 'SQL', 'CSS', 'PHP', 'HTML', 'JavaScript', 'Python']
lenguaje_actual = lenguajes[1]
print(f'El lenguaje que estoy estudiando hoy es {lenguaje_actual}')
print(f'El lenguaje que nos enseña Cuello es {lenguajes[0]}')
print(f'La longitud o tamaño del array es {len(lenguajes)}')

print('\nEste tipo de array en Python se denomina lista')
print(lenguajes)
print(lenguajes.index('Python'))
print(lenguajes.index('Python', 2))