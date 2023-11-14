import os
os.system('cls')


numeros = [1548, 52842, 973148, 5871, 69001, 4827, 963, 710, 7474, 397317]


def convertir_decimal_a_otro_sistema(base, decimal):
    hexadecimal = ''

    while True:
        cociente = decimal // base # división entera
        resto = decimal % base # resto de la división
        decimal = cociente

        if cociente < base:
            hexadecimal = obtener_digito_hexadecimal(cociente) + obtener_digito_hexadecimal(resto) + hexadecimal
            break
        else:
            hexadecimal = obtener_digito_hexadecimal(resto) + hexadecimal
            continue

    return hexadecimal


def obtener_digito_hexadecimal(digito_decimal):
    if digito_decimal == 10:
        return 'A'
    elif digito_decimal == 11:
        return 'B'
    elif digito_decimal == 12:
        return 'C'
    elif digito_decimal == 13:
        return 'D'
    elif digito_decimal == 14:
        return 'E'
    elif digito_decimal == 15:
        return 'F'
    else:
        return str(digito_decimal)


# print(obtener_digito_hexadecimal(15))
# print(convertir_decimal_a_hexadecimal(7843))

def convertir_numeros(numeros):
    hexadecimales = []
    for numero in numeros:
        hexadecimal = convertir_decimal_a_otro_sistema(2, numero)
        hexadecimales.append(hexadecimal)

    return hexadecimales


print(convertir_numeros(numeros))