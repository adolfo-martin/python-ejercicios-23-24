import os
os.system('cls')

def dividir(dividendo, divisor):
    if divisor == 0:
        # print('ERROR: No se puede dividor por cero.')
        # return 0
        # return False
        # return None OK
        raise Exception('No se puede dividor por cero.')
    else:
        cociente = dividendo / divisor
        return cociente

try:
    print(dividir(8, 2))
    print(dividir(8, 0))
except Exception as error: # catch
    print(f'ERROR: {error}')