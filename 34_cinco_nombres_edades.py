import os 
os.system('cls')

# nombres = []
# edades = []

# for i in range(0, 5):
#     nombre = input('Dime un nombre: ')
#     edad = int(input('Dime una edad: '))

#     nombres.append(nombre)
#     edades.append(edad)

# for i in range(0, 5):
#     print(f'La persona {nombres[i]} tiene {edades[i]} años.')


personas = []

# personas = [
#     [ 'pablo', 22 ],
#     [ 'sonia', 31 ],
#     [ 'andrea', 20 ],
#     [ 'santiago', 45 ]
# ]

for i in range(0, 5):
    nombre = input('Dime un nombre: ')
    edad = int(input('Dime una edad: '))

    personas[i][0] = nombre
    personas[i][1] = edad

for persona in personas:
    print(f'La persona {persona[0]} tiene {persona[1]} años.')