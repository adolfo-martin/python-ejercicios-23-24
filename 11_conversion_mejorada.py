import os

os.system('cls')


def cambiar_decimal_binario(numero_decimal):
    numero_binario = ''

    while True:
        cociente = numero_decimal // 2 # división entera
        resto = numero_decimal % 2 # resto de la división
        numero_decimal = cociente

        if cociente < 2:
            numero_binario = str(cociente) + str(resto) + numero_binario
            break
        else:
            numero_binario = str(resto) + numero_binario
            continue

    return numero_binario


numero_decimal = int(input('Introduce el número decimal: '))
numero_binario = cambiar_decimal_binario(numero_decimal)
print(numero_binario)