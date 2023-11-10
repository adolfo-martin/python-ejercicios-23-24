import os
os.system('cls')

animales = [ 'oveja', 'caballo', 'cerdo', 'gallina', 'pato' ]
animales.append('vaca')
animales.append('cabra')
animales.append('gato')
animales.insert(1, 'ratón')
print(animales)

animal = animales.pop()
print(animal)
print(animales)

animales.remove('caballo')
print(animales)

posicion_gallina = animales.index('gallina')
print(posicion_gallina)

print(animales[3])
animales[3] = 'pavo'
print(animales[3])
