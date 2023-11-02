# base_imponible = 70.5
# iva = 21.0

import os
os.system('cls')


def calcular_importe_total(base_imponible, iva):
    precio_total = base_imponible + (base_imponible * iva) / 100
    return precio_total

def calcular_impuestos()

precio = calcular_importe_total(70.5, 21.0)
print(precio)
