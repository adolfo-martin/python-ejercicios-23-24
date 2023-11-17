import os
os.system('cls')

colores_espaniol = ["Rojo", "Verde", "Azul", "Amarillo", "Negro", "Naranja", "Blanco", "Marrón"]
colores_ingles = ["Red", "Green", "Blue", "Yellow", "Black", "Orange", "White", "Brown"]
colores_frances = ["Rouge", "Vert", "Bleu", "Jaune", "Noir", "Orange", "Blanc", "Brun"]
colores_aleman = ["Rot", "Grün", "Blau", "Gelb", "Schwarz", "Orange", "Weiß", "Braun"]

def traducir_espaniol_ingles(palabra):
    for i in range(0, len(colores_espaniol)):
        if colores_espaniol[i] == palabra:
            return colores_ingles[i]

print(traducir_espaniol_ingles('Blanco'))


# print(colores_espaniol[0])
# print(colores_ingles[0])
# print(colores_frances[0])
# print(colores_aleman[0])

