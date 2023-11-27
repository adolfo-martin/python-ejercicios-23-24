import os, math
os.system('cls')

def calcular_raiz_mas(a, b, c):
    radicando = b ** 2 - 4 * a * c

    if radicando < 0:
        raise Exception('No existe la raiz porque el radicando es negativo.')
    else:
        raiz = (- b + math.sqrt(radicando)) / (2 * a) 
        return raiz


def calcular_raiz_menos(a, b, c):
    radicando = b ** 2 - 4 * a * c

    if radicando < 0:
        raise Exception('No existe la raiz porque el radicando es negativo.')
    else:
        raiz = (- b - math.sqrt(radicando)) / (2 * a) 
        return raiz
    

# try:
#     print(calcular_raiz_mas(64, 80, 25))
# except Exception as error:
#     print(f'ERROR: {error}')

# try:
#     print(calcular_raiz_menos(64, 80, 25))
# except Exception as error:
#     print(f'ERROR: {error}')

# try:
#     print(calcular_raiz_mas(64, 2, 25))
# except Exception as error:
#     print(f'ERROR: {error}')

# try:
#     print(calcular_raiz_menos(64, 2, 25))
# except Exception as error:
#     print(f'ERROR: {error}')

try:
    print(calcular_raiz_mas(64, 80, 25))
    print(calcular_raiz_menos(64, 80, 25))
    print(calcular_raiz_mas(64, 2, 25))
    print(calcular_raiz_menos(64, 2, 25))
except Exception as error:
    print(f'ERROR: {error}')

