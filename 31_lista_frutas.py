import os
os.system('cls')

frutas = ['pera', 'platano', 'manzana', 'fresa', 'limón']

frutas.append('mango')

print(frutas.index('fresa'))
# print(frutas.index('paraguayo'))

# for i in range(0,3):
#     fruta = input('Dame una fruta: ')
#     frutas.append(fruta)

# print(len(frutas))

frutas_nuevas = 0
while frutas_nuevas < 3:
    fruta_nueva = input('Dame una fruta: ')

    if fruta_nueva not in frutas:
        frutas.append(fruta_nueva)
        frutas_nuevas += 1
    else:
        print('Esa fruta ya existe en la lista.')
